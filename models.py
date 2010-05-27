from django.db import models

from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

from django.conf import settings

# Database value1 and value2 length can be specified in settings.py.  Default is 200
VALUE1SIZE = getattr(settings, 'ANALYTICS_VALUE1SIZE', 200)
VALUE2SIZE = getattr(settings, 'ANALYTICS_VALUE2SIZE', 200)


class Activity(models.Model):
    
    # These feilds are auto-filled with the request object
    ipaddr  = models.CharField(max_length = 39)
    session = models.CharField(max_length = Session._meta.fields[0].max_length) # Note: Using a CharField instead of FK here to avoid cascading deletes as deletes are common with the Session field
    user    = models.ForeignKey(User, blank=True, null=True)
    
    date    = models.DateTimeField(auto_now_add = True)

    # These fields are filled with our data
    subject = models.CharField(max_length = 100)
    value1  = models.CharField(max_length = VALUE1SIZE, blank=True, null=True)
    value2  = models.CharField(max_length = VALUE2SIZE, blank=True, null=True)
    
    def __init__(self, request, subject, value1='', value2 = '', *args, **kwargs):
        #self.subject = subject
        #self.value1 = value1
        #self.value2 = value2
        self.process_request(request)
        
        if self.user:
            kwargs['user_id'] = self.user.id

        kwargs['ipaddr'] = self.ipaddr
        kwargs['session'] = self.session
        kwargs['subject'] = subject
        kwargs['value1'] = value1
        kwargs['value2'] = value2

        return super(Activity, self).__init__(*args, **kwargs)
    
    def process_request(self, request):
        self.ipaddr = request.META['REMOTE_ADDR']
        self.session = request.session._session_key
        self.user = None
        if request.user.is_authenticated():
            self.user = request.user

        
    def save(self, *args, **kwargs):

        super(Activity, self).save(*args, **kwargs)
        return self


