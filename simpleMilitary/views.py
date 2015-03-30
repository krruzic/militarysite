from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template.response import TemplateResponse
from simpleMilitary.models import Personnel
from simpleMilitary.models import Person
# Create your views here.
#from django.utils
try:
  import simplejson as json
except ImportError:
  import json
from django.core import serializers
def index(request):
   fields    = {Person._meta.get_field("fname"),Person._meta.get_field("lname")}
   data      = json.loads(serializers.serialize("json", Person.objects.all().order_by('-sin')))

   def parse_data(data):

        result = []

        # flatten the dictionary
        def flatten_dict(d):
            def items():
                for key, value in d.items():
                    if isinstance(value, dict):
                        for subkey, subvalue in flatten_dict(value).items():
                            yield subkey, subvalue
                    else:
                        yield key, value

            return dict(items())

        for d in data:
            # change the 'pk' key name into its actual name in the database
            d[Personnel._meta.pk.name] = d.pop('pk')
            # append the flattend dict of each object's field-value to the result
            result.append(flatten_dict(d))

        return result


   context_instance = RequestContext(request, {
       'data'      : parse_data(data),
       'fields'    : fields,
   })
   return TemplateResponse(request, 'index.html', context_instance)



def searchResults(request):

    return render(request, 'searchResults.html', {})