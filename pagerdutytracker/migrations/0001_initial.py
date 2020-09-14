# Generated by Django 3.1.1 on 2020-09-14 09:03

from django.db import migrations, models
import django.db.models.deletion
import pagerdutytracker.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('routing_key', models.CharField(blank=True, default='fe9a080cf91acb8ed1891e6548f2ace3c66a109f', max_length=100, null=True)),
                ('incident_id', models.CharField(default=pagerdutytracker.models.Incident.increment_incident_number, editable=False, max_length=17, unique=True, verbose_name='IncidentID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('event_action', models.CharField(choices=[('trigger', 'trigger'), ('acknowledge', 'acknowledge'), ('resolve', 'resolve')], default='trigger', max_length=100, verbose_name='EventAction')),
                ('dedup_key', models.CharField(max_length=100, unique=True)),
                ('client', models.CharField(blank=True, max_length=100, null=True)),
                ('client_url', models.CharField(blank=True, max_length=100, null=True)),
                ('updated_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=1024, verbose_name='Title')),
                ('source', models.CharField(max_length=100, verbose_name='Source')),
                ('severity', models.CharField(choices=[('critical', 'critical'), ('error', 'error'), ('info', 'Info'), ('warning', 'warning')], default='warning', max_length=100, verbose_name='Severity')),
                ('timestamp', models.CharField(max_length=100, verbose_name='Timestamp')),
                ('component', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Component')),
                ('group', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='Group')),
                ('custom_details', models.TextField(blank=True, default=None, max_length=2500, null=True, verbose_name='CustomDetails')),
                ('class_name', models.CharField(blank=True, default=None, max_length=500, null=True, verbose_name='Class')),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_href', models.CharField(blank=True, max_length=200, null=True)),
                ('text', models.CharField(blank=True, max_length=100, null=True)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='pagerdutytracker.incident')),
            ],
        ),
        migrations.AddField(
            model_name='incident',
            name='payload',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pagerdutytracker.payload'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(blank=True, null=True, upload_to=pagerdutytracker.models.upload_location)),
                ('href', models.CharField(blank=True, max_length=200, null=True)),
                ('alt', models.CharField(blank=True, max_length=100, null=True)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='pagerdutytracker.incident')),
            ],
        ),
    ]
