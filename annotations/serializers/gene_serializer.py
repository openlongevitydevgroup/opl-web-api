from annotations.models.genes import Gene, GeneProblem
from annotations.serializers.base_serializer import BaseSerializer
from open_problems.serializers.OpenProblems import OpenProblemsSerializer


class GeneSerializer(BaseSerializer):
    class Meta(BaseSerializer.Meta):
        model = Gene
        fields = "__all__"


class GeneProblemlSerializer(BaseSerializer):
    gene_id = GeneSerializer()
    open_problem = OpenProblemsSerializer()

    class Meta(BaseSerializer.Meta):
        model = GeneProblem
