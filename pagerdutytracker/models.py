from django.db import models
from enum import Enum
from django.conf import settings
import json
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver


# Create your models here.

######################################################
# Core Issue models
#######################################################


INCIDENT_STATUS_CHOICES = (
    ('trigger', 'trigger'),
    ('acknowledge', 'acknowledge'),
    ('resolve', 'resolve'),
)

INCIDENT_SEVERITY_CHOICES = (
    ('critical', 'critical'),
    ('error', 'error'),
    ('info', 'Info'),
    ('warning', 'warning'),
)

def upload_location(instance, filename):
    file_path = 'incident/{author_id}/{title}-{filename}'.format(
                author_id=str(instance.incident.creator.email),title=str(instance.incident.payload.summary), filename=filename)
    return file_path

class Payload(models.Model):
    """
    """

    summary         = models.CharField(max_length=100, verbose_name="Title", null=False, blank=False)
    source          = models.CharField(max_length=100, verbose_name="Source", null=False, blank=False)
    severity        = models.CharField(max_length=100, choices=INCIDENT_SEVERITY_CHOICES, default='warning', verbose_name="Severity")
    timestamp       = models.CharField(max_length=100, verbose_name="Timestamp",null=False, blank=False)
    component       = models.CharField(max_length=100, verbose_name="Component", null=True, blank=True, default=None)
    group           = models.CharField(max_length=100, verbose_name="Group", null=True, blank=True, default=None)
    custom_details  = models.TextField(max_length=2500, verbose_name="CustomDetails", null=True, blank=True, default=None)
    class_name      = models.CharField(max_length=500, verbose_name="Class", null=True, blank=True, default=None)



class Incident(models.Model):
    '''
    The core model for this project, representing a bug, feature request,
    or some other completable task.
    :creator: User that submitted the issue.
    :owner: A user that has taken responsibility for resolving the issue.
    :users: Users that are "watching" the issue.
    :category: Searchable term that succintly groups the issue with related issues.
    :title: Short description that fits on a post-it card.
    :desc: Long description.
    :priority: Severity of issue from 1-5.
    :log_entries: 1:Many link to IssueLogEntry.
        Used for posting short memos to the issue page for others to view.
    '''

    def increment_incident_number():
        last_incident_id = Incident.objects.all().order_by('id').last()

        if not last_incident_id:
            return 'INC-'+ '0001'

        help_id = last_incident_id.incident_id
        help_int = help_id[5:9]
        new_help_int = int(help_int) + 1
        new_help_id = 'INC-' + str(new_help_int).zfill(4)
        return new_help_id

    routing_key     = models.CharField(max_length=100,default="fe9a080cf91acb8ed1891e6548f2ace3c66a109f",null=True, blank=True)
#    creator         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default="karthch2")
    incident_id     = models.CharField(max_length=17, unique=True, default=increment_incident_number, editable=False, verbose_name="IncidentID")
    created         = models.DateTimeField(auto_now_add=True, verbose_name="Created")
#    assigned        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_DEFAULT, default="karthch2", verbose_name="assigned", related_name="%(class)ss_joined")
    event_action    = models.CharField(max_length=100, choices=INCIDENT_STATUS_CHOICES, default='trigger', verbose_name="EventAction")
    dedup_key       = models.CharField(max_length=100, unique=True, null=False, blank=False)
    payload         = models.OneToOneField(Payload, on_delete=models.CASCADE)
    client          = models.CharField(max_length=100, null=True, blank=True)
    client_url      = models.CharField(max_length=100, null=True, blank=True)
    updated_on      = models.DateField(auto_now=True)


    def __str__(self):
        return self.payload.summary

class Link(models.Model):

    link_href = models.CharField(max_length=200, null=True, blank=True)
    text = models.CharField(max_length=100, null=True, blank=True)
    incident = models.ForeignKey(Incident, related_name='links', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

class Image(models.Model):
    src  = models.ImageField(upload_to=upload_location, null=True, blank=True)
    href = models.CharField(max_length=200, null=True, blank=True)
    alt  = models.CharField(max_length=100, null=True, blank=True)

    incident = models.ForeignKey(Incident, related_name='images', on_delete=models.CASCADE)
    def __str__(self):
        return self.href



@receiver(post_delete, sender=Image)
def submission_delete(sender, instance, **kwargs):
    instance.src.delete(False)


@receiver(post_delete, sender=Incident)
def post_delete_user(sender, instance, *args, **kwargs):
    if instance.payload: # just in case user is not specified
        instance.payload.delete()
