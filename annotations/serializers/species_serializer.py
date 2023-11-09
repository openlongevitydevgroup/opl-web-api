from annotations.models.species import Species, SpeciesProblems
from annotations.serializers.base_serializer import BaseSerializer
from open_problems.serializers.OpenProblems import OpenProblemsSerializer


class SpeciesSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Species
        fields = "__all__"


class SpeciesProblemSerializer(BaseSerializer):
    species = SpeciesSerializer()
    open_problem = OpenProblemsSerializer()

    class Meta(BaseSerializer.Meta):
        model = SpeciesProblems
        fields = "__all__"
