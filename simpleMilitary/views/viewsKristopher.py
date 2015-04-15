from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
from simpleMilitary.models import Personnel
from simpleMilitary.models import Veteran
from simpleMilitary.models import AuthorizedToUse
from simpleMilitary.models import AwardedTo
from simpleMilitary.forms import RegistrationForm
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import logout
import json
import datetime

@login_required
def personnelDetail(request, personnel_sin):
    SIN_user = False
    if request.user.is_authenticated():
        SIN_user = request.user.username[0].isdigit()
    try:
        personnel = Personnel.objects.select_related('uid__bid', 'psin').get(pk=personnel_sin)
        weapons = AuthorizedToUse.objects.distinct().filter(psin=personnel_sin)
        awards = AwardedTo.objects.distinct().filter(sin=personnel_sin)
    except Personnel.DoesNotExist:
        raise Http404("No such personnel")
    if personnel.psin.sin != request.user.username and not request.user.is_staff:
        return HttpResponseForbidden()
    pname = personnel.psin.fname + " " + personnel.psin.lname
    properties = {
        'username': request.user.username,
        'super': request.user.is_staff,
        'active_page': 'personnel details', # set this as the TEXT the navbar displays
        'logged_in': True,
        'personnel': pname,
        'SIN_user': SIN_user
    }
    return render(request, 'personnel/detail.html', {'personnel': personnel, 'weapons': weapons, 'awards': awards, 'properties': properties})

def login_user(request):
    SIN_user = False
    if request.user.is_authenticated():
        SIN_user = request.user.username[0].isdigit()
    properties = {
        'username': request.user.username,
        'super': request.user.is_staff,
        'active_page': 'Login', # set this as the TEXT the navbar displays
        'logged_in': request.user.is_authenticated(),
        'personnel': '',
        'SIN_user': SIN_user,
        'hide_drops': True,
    }
    c = {}
    c.update(csrf(request))
    state = None
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if request.GET.get('next', False):
                    return HttpResponseRedirect(request.GET.get('next'))
                else:
                    return HttpResponseRedirect('/simpleMilitary/')
            else:
                state = "Your account is not active, please register or contact the admin."
        else:
            state = "Your username and/or password were incorrect."
    print state
    return render(request, 'registration/login.html', {'state':state, 'username': username, 'properties': properties})

def register_page(request):
    SIN_user = False
    if request.user.is_authenticated():
        SIN_user = request.user.username[0].isdigit()
    properties = {
        'username': request.user.username,
        'super': request.user.is_staff,
        'active_page': 'Registration', # set this as the TEXT the navbar displays
        'logged_in': request.user.is_authenticated(),
        'personnel': '',
        'SIN_user': SIN_user,
        'hide_drops': True,
    }
    c = {}
    error = None
    form = RegistrationForm()
    c.update(csrf(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            isStaff = False
            print "Registered" + form.cleaned_data['username']
            personnel = Personnel.objects.get(pk=form.cleaned_data['username'])
            if (personnel.rank == 'General'):
                isStaff = True
            user = User.objects._create_user(
                                            form.cleaned_data['username'],
                                            None,
                                            form.cleaned_data['password1'],
                                            isStaff,
                                            isStaff
                                            )
            return HttpResponseRedirect('/simpleMilitary/')
        else:
            error = "SIN has been registered or does not exist"
            if (form.cleaned_data['password1'] != form.cleaned_data['password2']):
                if error:
                    error = error + ", and the passwords didn't match"
                else:
                    error = "Passwords don't match"
            form = RegistrationForm()
    return render(request, 'registration/register.html', {"form": form, "error": error, 'properties': properties})

def logout_user(request):
    SIN_user = False
    if request.user.is_authenticated():
        SIN_user = request.user.username[0].isdigit()
    properties = {
        'username': request.user.username,
        'super': request.user.is_staff,
        'active_page': 'Logout', # set this as the TEXT the navbar displays
        'logged_in': request.user.is_authenticated(),
        'personnel': '',
        'SIN_user': SIN_user,
        'hide_drops': True,
    }
    logout(request)
    return render(request, 'registration/logout.html', {'properties': properties})



@login_required
def admin_operations(request):
    c = {}
    c.update(csrf(request))
    SIN_user = False
    if request.user.is_authenticated():
        SIN_user = request.user.username[0].isdigit()
    properties = {
        'username': request.user.username,
        'super': request.user.is_staff,
        'active_page': 'Admin Operations', # set this as the TEXT the navbar displays
        'logged_in': request.user.is_authenticated(),
        'personnel': '',
        'SIN_user': SIN_user
    }
    personnel = Personnel.objects.all().order_by('psin__fname').select_related('psin')

    if request.user.is_staff:
        print "Administrator!"
    else:
        return HttpResponseForbidden()
    post_text = "SADF"
    if request.is_ajax():
        print "AJAX"
        response_data = {}
        response_data['people'] = ["-1"]
        print request.POST.getlist('selected[]')
        if request.POST.getlist('selected[]') == []:
            return HttpResponse(
                json.dumps(response_data),
                "application/json"
            )
        for sin in request.POST.getlist('selected[]'):
            p = Personnel.objects.get(pk=sin).select_related('psin')
            print("line 1")
            response_data['people'].append(p.psin.fname + " " + p.psin.lname)
            print("line 2")
            day = datetime.date.today()
            v = Veteran(pk=p.psin, end_date=day)
            v.save()
            print("saved vet")
            p.delete()
            print("delete personnel")
        del response_data['people'][0]
        response_data['people'][-1] = response_data['people'][-1].replace(", ", "")
        return HttpResponse(
            json.dumps(response_data),
            "application/json"
        )
    print post_text
    return render(request, 'adminOps.html', {'personnel': personnel, 'properties': properties, 'c': c})

@login_required
def all_personnel(request):
    SIN_user = False
    if request.user.is_authenticated():
        SIN_user = request.user.username[0].isdigit()
    properties = {
        'username': request.user.username,
        'super': request.user.is_staff,
        'active_page': 'All Personnel', # set this as the TEXT the navbar displays
        'logged_in': request.user.is_authenticated(),
        'personnel': '',
        'SIN_user': SIN_user
    }
    if not request.user.is_staff:
        print "Not superuser, don't show this page"
    p = Personnel.objects.all().select_related('uid__bid', 'psin')
    return render(request, 'personnel/all.html', {'users': p, 'properties': properties})

