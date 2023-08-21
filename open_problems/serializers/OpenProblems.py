from rest_framework import serializers
from open_problems.models.open_problems import OpenProblems
from utils.recursive_serializer import RecursiveSerializer


class OpenProblemsSerializer(serializers.ModelSerializer):
    children = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = OpenProblems
        fields = ["problem_id", "title", "description",
                  "contact", "parent_problem", "descendants_count", "children"]


class DescendantsDescendingSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = OpenProblems
        fields = ["problem_id", "title", "description",
                  "contact", "parent_problem", "descendants_count", "children"]

    def get_children(self, instance):
        ordered_children = instance.children.all().order_by('-descendants_count')
        serializer = DescendantsDescendingSerializer(
            ordered_children, many=True, context=self.context)
        return serializer.data





