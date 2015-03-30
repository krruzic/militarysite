from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.template.response import TemplateResponse
from simpleMilitary.models import Personnel
from simpleMilitary.models import Person
from django.http import Http404
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf

from django.core import serializers

@login_required
def index(request):
    names     = []
    fields = {"First Name", "Last Name", "Base", "PSIN"}
    for p in Personnel.objects.all().order_by('psin__fname'):
        try:
            bname = p.uid.bid.bname
        except:
            bname = "NULL"
        names.append({"First Name": p.psin.fname, "Last Name": p.psin.lname, "Base": bname, "PSIN": p.psin})

    return render(request, 'index.html', {'data': names, 'fields': fields})

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


def searchResults(request):

    return render(request, 'searchResults.html', {})
    names     = []
    fields = {"First Name", "Last Name", "Base"}
    for p in Personnel.objects.all().order_by('psin__fname'):
        try:
            bname = p.uid.bid.bname
        except:
            bname = "NULL"
        names.append({"First Name": p.psin.fname, "Last Name": p.psin.lname, "Base": bname})

    context_instance = RequestContext(request, {
        'data'      : names,
        'fields'    : fields,
    })
    return TemplateResponse(request, 'index.html', context_instance)