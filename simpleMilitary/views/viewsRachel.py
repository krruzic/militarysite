from django.shortcuts import render
from django.template import RequestContext
from simpleMilitary.models import Personnel
from simpleMilitary.models import Veteran
from simpleMilitary.models import Conflict
from django.shortcuts import render
from django.db import connection
from django.db.models import Q



def index(request):
    SIN_user = False
    if request.user.is_authenticated():
        SIN_user = request.user.username[0].isdigit()

    properties = {
        'username': request.user.username,
        'super': request.user.is_staff,
        'active_page': 'Home', # set this as the TEXT the navbar displays
        'logged_in': request.user.is_authenticated(),
        'personnel': '',
        'SIN_user': SIN_user
    }
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
    ps = Personnel.objects.all().order_by('psin__fname').select_related('uid__bid', 'psin')
    for p in ps:
        try:
            bname = p.uid.bid.bname
        except:
            bname = ""
        pnames.append({"First Name": p.psin.fname, "Last Name": p.psin.lname, "Base": bname})
    vnames     = []
    vfields = {"First Name", "Last Name", "End Date"}
    for p in Veteran.objects.all().order_by('vsin__fname').select_related('vsin'):
        vnames.append({"First Name": p.vsin.fname, "Last Name": p.vsin.lname, "End Date": p.end_date})
    return render(request, 'index.html',
        {'pdata': pnames, 'pfields': pfields, 'vdata': vnames, 'vfields': vfields,
         'new_recruits': new_recruits, 'conflicts': conflicts, 'active_duty': active_duty,
         'per_unit': per_unit, 'ave_age': ave_age, 'properties': properties})

    # return render(request, 'index.html', {'data': names, 'fields': fields, 'properties': properties})

def searchResults(request):
    SIN_user = False
    if request.user.is_authenticated():
        SIN_user = request.user.username[0].isdigit()
    properties = {
        'username': request.user.username,
        'super': request.user.is_staff,
        'active_page': 'Search Results', # set this as the TEXT the navbar displays
        'logged_in': request.user.is_authenticated(),
        'personnel': '',
        'SIN_user': SIN_user
    }
    results = request.GET.get('q')
    pnames     = []
    vnames     = []
    pfields = {"First Name", "Last Name", "Base"}
    vfields = {"First Name", "Last Name", "End Date"}
    for p in Personnel.objects.order_by('psin__fname').filter(Q(psin__fname__icontains=results) | Q(psin__lname__icontains=results)).select_related('uid__bid', 'psin'):
        try:
            bname = p.uid.bid.bname
        except:
            bname = ""
        pnames.append({"First Name": p.psin.fname, "Last Name": p.psin.lname, "Base": bname})
    for p in Veteran.objects.order_by('vsin__fname').filter(Q(vsin__fname__icontains=results) | Q(vsin__lname__icontains=results)).select_related('vsin'):
        vnames.append({"First Name": p.vsin.fname, "Last Name": p.vsin.lname, "End Date": p.end_date})
    context_instance = RequestContext(request, {
        'pdata'      : pnames,
        'pfields'    : pfields,
        'vdata'      : vnames,
        'vfields'    : vfields,
    })
    return render(request, 'index.html', {'pdata': pnames, 'pfields': pfields, 'vdata': vnames, 'vfields': vfields, 'properties': properties})
