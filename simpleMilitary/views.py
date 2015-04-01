from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.template.response import TemplateResponse
from simpleMilitary.models import Personnel
from simpleMilitary.models import Veteran
from simpleMilitary.models import Person
from simpleMilitary.models import Conflict
from django.db.models import Avg
from django.http import Http404
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.core.context_processors import csrf
from django.db import connection, transaction
from django.db.models import Q
import math

from django.core import serializers

def index(request):
    pnames     = []
    pfields = {"First Name", "Last Name", "Base"}
    new_recruits = {Personnel.objects.filter(status='New Recruit').count()}
    conflicts = {Conflict.objects.filter(status='Ongoing').count()}
    active_duty = {Personnel.objects.filter(status='Active Duty').count()}
    cursor = connection.cursor()
    cursor.execute("SELECT AVG(units.count) FROM (SELECT COUNT(*) AS count FROM PERSONNEL WHERE uid IS NOT NULL GROUP BY uid) AS units")
    row = cursor.fetchone()
    if row:
      per_unit = {str(int(round(row[0])))}
    else:
      per_unit = {0}
    cursor.execute("SELECT AVG(p.YearDiff) FROM (SELECT (DATEDIFF(NOW(), bdate)/365) AS YearDiff FROM PERSONNEL, PERSON WHERE psin=sin) AS p")
    row = cursor.fetchone()
    if row:
      ave_age = {str(int(round(row[0])))}
    else:
      ave_age = {0}
    print 'hi'
    print ave_age
    for p in Personnel.objects.all().order_by('psin__fname'):
        try:
            bname = p.uid.bid.bname
        except:
            bname = ""
        pnames.append({"First Name": p.psin.fname, "Last Name": p.psin.lname, "Base": bname})
    vnames     = []
    vfields = {"First Name", "Last Name", "End Date"}
    for p in Veteran.objects.all().order_by('vsin__fname'):
        vnames.append({"First Name": p.vsin.fname, "Last Name": p.vsin.lname, "End Date": p.end_date})
    return render(request, 'index.html', {'pdata': pnames, 'pfields': pfields, 'vdata': vnames, 'vfields': vfields, 'new_recruits': new_recruits, 'conflicts': conflicts, 'active_duty': active_duty, 'per_unit': per_unit, 'ave_age': ave_age})


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
    results = request.GET.get('q')
    pnames     = []
    vnames     = []
    pfields = {"First Name", "Last Name", "Base"}
    vfields = {"First Name", "Last Name", "End Date"} 
    for p in Personnel.objects.order_by('psin__fname').filter(Q(psin__fname__contains=results) | Q(psin__lname__contains=results)):
        try:
            bname = p.uid.bid.bname
        except:
            bname = ""
        pnames.append({"First Name": p.psin.fname, "Last Name": p.psin.lname, "Base": bname})
    for p in Veteran.objects.order_by('vsin__fname').filter(Q(vsin__fname__icontains=results) | Q(vsin__lname__icontains=results)):
        vnames.append({"First Name": p.vsin.fname, "Last Name": p.vsin.lname, "End Date": p.end_date})    
    context_instance = RequestContext(request, {
        'pdata'      : pnames,
        'pfields'    : pfields,
        'vdata'      : vnames,
        'vfields'    : vfields,
    })
    return render(request, 'index.html', {'pdata': pnames, 'pfields': pfields, 'vdata': vnames, 'vfields': vfields})