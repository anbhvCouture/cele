from math import frexp
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .tasks import prnt

@api_view(['POST'])
def postData(request):
    prnt.delay(request.data)
    return Response(request.data)
