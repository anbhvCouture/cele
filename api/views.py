from math import frexp
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def postData(request):
    print(request.data)
    return Response(request.data)
