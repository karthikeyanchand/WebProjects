"""pagerduty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken.views import obtain_auth_token
#from rest_framework.authtoken import views
from pagerdutytracker.views import IncidentListView

schema_view = get_schema_view(title='PagerDuty API',
                description='An API to create incideng tickets.')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/api/v2/pagerduty/', include('pagerdutytracker.api.urls', 'pagerduty_api')),
    path('schema/', schema_view),
	path('docs/', include_docs_urls(title='PagerDuty API')),
	path('',IncidentListView.as_view(), name='view'),

]
