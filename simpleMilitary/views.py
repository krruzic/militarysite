from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template.response import TemplateResponse
from simpleMilitary.models import Personnel
from simpleMilitary.models import Person



import simplejson as json
from django.core import serializers
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