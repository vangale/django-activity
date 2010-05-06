from django.conf.urls.defaults import *

urlpatterns = patterns('activity.views', 
                       (r'^request/', 'request', {})
)
