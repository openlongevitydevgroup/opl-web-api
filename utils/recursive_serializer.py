from rest_framework import serializers


# Serializer to retrieve children of parent node
class RecursiveSerializer(serializers.Serializer):
    ''' Handle self-nested serializer'''

    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(
            instance, context=self.context)
        return serializer.data
