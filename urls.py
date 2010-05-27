from django.conf.urls.defaults import *

urlpatterns = patterns(
    'djangoactivity.views', 
    (r'^request/', 'request', {}),
    (r'^record/', 'record', {}),
    
    
)
