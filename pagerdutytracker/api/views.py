from rest_framework import viewsets 
from rest_framework.views import APIView
#from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
#from rest_framework_api_key.permissions import HasAPIKey
from pagerdutytracker.models import Incident,Link,Image,Payload
from pagerdutytracker.api.serializers import LinkSerializer, ImageSerializer, PayloadSerializer, IncidentSerializer


class LinkViewset(viewsets.ModelViewSet):
	queryset = Link.objects.all()
	serializer_class = LinkSerializer

class ImageViewset(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class PayloadViewset(viewsets.ModelViewSet):
	queryset = Payload.objects.all()
	serializer_class = PayloadSerializer

class IncidentViewset(viewsets.ModelViewSet):
	queryset = Incident.objects.all()
	serializer_class = IncidentSerializer


class HelloView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)