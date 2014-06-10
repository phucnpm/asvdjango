from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

def mydojo(request):
    return render_to_response('demo/mydojo.html', context_instance=RequestContext(request))