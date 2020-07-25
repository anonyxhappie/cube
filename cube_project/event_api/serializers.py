from rest_framework import serializers

class EventSerializer(serializers.Serializer):
    userid = serializers.IntegerField()
    ts = serializers.CharField(max_length=255)
    latlong = serializers.CharField(max_length=255)
    noun = serializers.CharField(max_length=10)
    verb = serializers.CharField(max_length=10)
    timespent = serializers.IntegerField(allow_null=True)
    properties = serializers.JSONField()