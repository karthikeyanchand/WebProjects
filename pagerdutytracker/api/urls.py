from django.urls import include, path
from django.conf.urls import url
# from pagerdutytracker.api.views import(
# 	api_create_issue_view
# )
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from pagerdutytracker.api import views

app_name = 'pagerdutytracker'



router = DefaultRouter()
router.register(r'enqueue', views.IncidentViewset)
#router.register(r'payload', views.PayloadViewset)
#router.register(r'image', views.ImageViewset)
#router.register(r'link', views.LinkViewset)
#router.register(r'hello', views.HelloView)

# urlpatterns = [
# 	path('enqueue/', views.IncidentViewset.as_view({'get': 'list', 'post': 'create'}), name='enqueue'),
# 	path('payload/', views.PayloadViewset.as_view({'get': 'list', 'post': 'create'}), name='payload'),
# 	path('image/', views.ImageViewset.as_view({'get': 'list', 'post': 'create'}), name='image'),
# 	path('link/', views.LinkViewset.as_view({'get': 'list', 'post': 'create'}), name='link'),
# 	path('hello/', views.HelloView.as_view(), name='hello'),

# ]

urlpatterns = [
	#path('hello/', views.HelloView.as_view(), name='hello'),
	url(r'', include(router.urls)),
	
]