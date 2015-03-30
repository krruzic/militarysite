from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.template.response import TemplateResponse
from simpleMilitary.models import Personnel
from simpleMilitary.models import Person
# Create your views here.
#from django.utils
import simplejson as json
from django.core import serializers
def index(request):
   fields    = Personnel._meta.fields
   data      = json.loads(serializers.serialize("json", Personnel.objects.all()))

   def parse_data(data):

        result = []

        # flatten the dictionary
        def flatten_dict(d):
            """
            Because the only nested dict here is the fields, let's just
            remove the 'fields' suffix so that the fields can be loaded in
            template by name
            """
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
            d[Person._meta.pk.name] = d.pop('pk')
            # append the flattend dict of each object's field-value to the result
            result.append(flatten_dict(d))

        return result


   context_instance = RequestContext(request, {
       'data'      : parse_data(data),
       'fields'    : fields,
   })
   return TemplateResponse(request, 'index.html', context_instance)