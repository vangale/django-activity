
from djangoactivity.models import Activity
import re

from django.conf import settings

class PageActivity:

    def process_response(self, request, response):

        if hasattr(request, 'page_activity_recorded'):
            print "already recorded..."
            return 
        

        print "recording page activity"
        referer = request.META.get('HTTP_REFERER', '')
        page = request.get_full_path()
        print referer, page
        
        # Use the following if statement if you are also serving media files (usual dev version only)
        if not (re.search("\.[js|png|jpg|css|ico]", page)) and not re.search("/djscript/", page):
            print "saving!"
            activity = Activity(request, 'pages', page, referer).save()
            print "saved", Activity.objects.all().count(), activity.id
            
        
        request.page_activity_recorded = False
        

        return response
