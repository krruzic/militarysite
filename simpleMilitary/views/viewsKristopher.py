from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseForbidden
from simpleMilitary.models import Personnel
from simpleMilitary.models import AuthorizedToUse
from simpleMilitary.forms import RegistrationForm
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


@login_required
def personnelDetail(request, personnel_sin):
    # if request.user.username != personnel_sin:
    #     return HttpResponseForbidden()
    try:
        personnel = Personnel.objects.get(pk=personnel_sin)
        weapons = AuthorizedToUse.objects.distinct().filter(psin=personnel_sin)
    except Personnel.DoesNotExist:
        raise Http404("No such personnel")
    pname = personnel.psin.fname + " " + personnel.psin.lname
    properties = {
        'username': request.user.username,
        'super': request.user.is_superuser,
        'searchable': False,
        'active_page': 'Information for ' + pname, # set this as the TEXT the navbar displays
        'logged_in': True,
        'personnel': pname
    }
    return render(request, 'personnel/detail.html', {'personnel': personnel, 'weapons': weapons, 'properties': properties})

def login_user(request):
    c = {}
    c.update(csrf(request))
    state = "Please log in below..."
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
                    return HttpResponseRedirect('/login/')
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render(request, 'auth.html', {'state':state, 'username': username})

def register_page(request):
    c = {}
    error = ""
    c.update(csrf(request))
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            isStaff = 0
            print "Registered" + form.cleaned_data['username']
            personnel = Personnel.objects.get(pk=form.cleaned_data['username'])
            if (personnel.rank == 'General'):
                isStaff = 1
            user = User.objects.create_user(
                                            username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'],
                                            is_staff=isStaff
                                            )
            return HttpResponseRedirect('/simpleMilitary/')
    else:
        form = RegistrationForm()
        error = "Invalid registration form"
    return render(request, 'registration/register.html', {"form": form, "error": error})

@login_required
@csrf_exempt
def admin_operations(request):
    if request.user.is_superuser:
        print "Administrator!"
    post_text = "SADF"
    if request.method == 'POST':
        post_text = "YA"
    print post_text
    # if(request.GET.get('my-btn')):
    #     print "Button pressed!!"
        # mypythoncode.mypythonfunction( int(request.GET.get('mytextbox')) )
    # try:
    #     personnels = Personnel.objects.all().values()
    #     weapons = AuthorizedToUse.objects.filter(psin=personnel_sin)
    # except Personnel.DoesNotExist:
    #     raise Http404("No such personnel")
    return render(request, 'adminOps.html', {})

@login_required
def all_personnel(request):
    if not request.user.is_superuser:
        print "Not superuser, don't show this page"
    p = Personnel.objects.all()
    return render(request, 'personnel/all.html', {'users': p})