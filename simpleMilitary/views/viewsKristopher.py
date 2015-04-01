from django.shortcuts import render
from django.http import HttpResponseRedirect
from simpleMilitary.models import Personnel
from simpleMilitary.forms import RegistrationForm
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf

from django.contrib.auth.models import User


@login_required
def personnelDetail(request, personnel_sin):
    try:
        personnel = Personnel.objects.get(pk=personnel_sin)
    except Personnel.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'personnel/detail.html', {'personnel': personnel})

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
    print "TEST"
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print "TEST2"
        if form.is_valid():
            print "Registered" + form.cleaned_data['username']
            user = User.objects.create_user(
                                            username=form.cleaned_data['username'],
                                            password=form.cleaned_data['password1'],
                                            )
            return HttpResponseRedirect('/simpleMilitary/')
    else:
        form = RegistrationForm()
        error = "Invalid registration form"
    return render(request, 'register.html', {"form": form, "Error": error})
