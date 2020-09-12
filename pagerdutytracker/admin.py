from django.contrib import admin

# Register your models here.

from pagerdutytracker.models import Incident,Link,Image,Payload


admin.site.register(Incident)
admin.site.register(Link)
admin.site.register(Image)
admin.site.register(Payload)