import django_tables2 as tables
from pagerdutytracker.models import Incident
from enum import Enum



class PagerSemanticTable(tables.Table):

    #incident_id = tables.Column(linkify=True)
    summary = tables.Column(accessor='payload.summary')
    source = tables.Column(accessor='payload.source')
    severity = tables.Column(accessor='payload.severity')
    timestamp = tables.Column(accessor='payload.timestamp')


    class Meta:
        model = Incident
        template_name = "django_tables2/semantic.html"
        exclude = ("created","id","updated_on","routing_key","dedup_key","payload","client","client_url")