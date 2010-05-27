# Create your views here.

from django.shortcuts import render_to_response
from django.http import HttpResponse, Http404

def request(request):

    return HttpResponse('request Meta: ' + str(request.META) + "\n\n" + str(request.session._session_key))
    


from djangoactivity.models import Activity


def record(request):
    
    subject = request.GET.get('subject', "")
    value1  = request.GET.get('value1', "")
    value2  = request.GET.get('value2', "")

    if not subject:
        raise Http404
    
    activity = Activity(request, subject, value1, value2).save()

    return HttpResponse('success', mimetype='application/javascript')
