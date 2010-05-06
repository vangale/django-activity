
from activity.models import Activity
import re

from django.conf import settings

class PageActivity:

    def process_request(self, request):
        referer = request.META.get('HTTP_REFERER', '').replace(settings.SITE_URL, '')
        page = request.get_full_path()
        
        # Use the following if statement if you are also serving media files (usual dev version only)
        if not (re.search("\.[js|png|jpg|css]", page)):
            activity = Activity(request, 'pages', page, referer).save()
            
            
        
        
        
