from .filter_annotations import filter_by_annotations
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from open_problems.serializers import OPSerializer

@api_view(["GET"])
def filter_annotations(request):
    if request.method == "GET":
        annotations = request.GET
        try:
            open_problems_filtered = filter_by_annotations(annotations)
            serializer = OPSerializer(open_problems_filtered, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e: 
            print(str(e))
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
            

    
