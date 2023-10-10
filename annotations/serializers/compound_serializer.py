from annotations.models.compounds import Compounds, CompoundProblems
from .base_serializer import BaseSerializer
from open_problems.serializers.OpenProblems import OpenProblemsSerializer


class CompoundsSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Compounds


class CompoundProblemSerializer(BaseSerializer):
    compound = CompoundsSerializer()
    open_problem = OpenProblemsSerializer()

    class Meta(BaseSerializer.Meta):
        model = CompoundProblems
