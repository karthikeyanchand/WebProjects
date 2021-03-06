from pagerdutytracker.models import Incident,Link,Image,Payload
from rest_framework import serializers
from django.conf import settings
import logging
import json
logger = logging.getLogger("mylogger")
from rest_framework import status
from rest_framework.response import Response
from drf_writable_nested.mixins import UniqueFieldsMixin, NestedUpdateMixin, NestedCreateMixin


def routing_field_restriction(rk):
	if rk != "fe9a080cf91acb8ed1891e6548f2ace3c66a109f":
		raise serializers.ValidationError("Authorization error!!! Please check the routing_key")
	else:
		return rk

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('link_href', 'incident', 'text')
        read_only_fields = ('incident',)

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('src', 'href', 'incident', 'alt')
        read_only_fields = ('incident',)

class PayloadSerializer(serializers.ModelSerializer):
	custom_details = serializers.JSONField()
	class Meta:
		model = Payload
		fields = ('summary', 'source', 'severity', 'timestamp', 'component','group','custom_details','class_name')


class IncidentSerializer(UniqueFieldsMixin, NestedUpdateMixin,NestedCreateMixin,serializers.ModelSerializer):
	

	payload  = PayloadSerializer()
	links    = LinkSerializer(many=True,required=False)
	images   = ImageSerializer(many=True,required=False)
	routing_key = serializers.CharField(validators=[routing_field_restriction])
	id = serializers.ReadOnlyField()
	class Meta:
		model = Incident

		fields = ('id','routing_key','event_action', 'dedup_key', 'payload', 'links', 'images', 'client', 'client_url')

		

	def destroy(self, request, *args, **kwargs):
		try:
			instance = self.get_object()
			self.perform_destroy(instance)
		except Http404:
			pass
		content = {"status":"Record deleted Succesfully."}
		return Response(content,status=status.HTTP_200_OK)

	def perform_destroy(self, instance):
		instance.delete()


