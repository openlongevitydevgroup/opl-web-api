from rest_framework import serializers

class BaseSerializer(serializers.Serializer): 
    class Meta: 
        fields = "__all__"
