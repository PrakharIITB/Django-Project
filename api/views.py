from rest_framework.response import Response
from rest_framework.decorators import api_view
from Home.models import team
from .serializer import teamSerializer

@api_view(['GET'])
def getData(request):
    data = team.objects.all()
    serializer = teamSerializer(data, many=True)
    return Response(serializer.data)
