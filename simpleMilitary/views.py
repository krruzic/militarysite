from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template.response import TemplateResponse
from simpleMilitary.models import Personnel
from simpleMilitary.models import Person
from django.http import Http404
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

import simplejson as json
from django.core import serializers
@login_required
def index(request):
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


def personnelDetail(request, personnel_sin):
    try:
        personnel = Personnel.objects.get(pk=personnel_sin)
    except Personnel.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'personnel/detail.html', {'personnel': personnel})