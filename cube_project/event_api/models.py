from django.db import models

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    userid = models.IntegerField(editable=False)
    ts = models.CharField(max_length=255, editable=False)
    latlong = models.CharField(max_length=255, editable=False)
    noun = models.CharField(max_length=10, editable=False)
    verb = models.CharField(max_length=10, editable=False)
    timespent = models.IntegerField(null=True, editable=False)
    properties = models.TextField(editable=False)
    

class EventRules(models.Model):
    event_rule_id = models.AutoField(primary_key=True)
    rule_name = models.CharField(unique=True, max_length=255, editable=False)
    rule_description = models.TextField(editable=False)
    is_active = models.BooleanField(default=True)
