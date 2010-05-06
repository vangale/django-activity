# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse

def request(request):
    return HttpResponse('request Meta: ' + str(request.META) + "\n\n" + str(request.session._session_key))
    
