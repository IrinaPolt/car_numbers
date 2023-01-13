from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserSerializer, PlateSerializer
from plates.models import Plate

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def plates_list(request):
    plates = Plate.objects.all()
    serializer = PlateSerializer(plates, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def plate_add(request):
    serializer = PlateSerializer(data=request.data, )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def plates_generate(request):
    # amount = request.data['amount'] # или query_params?
    # serializer = PlateSerializer(data=request.data, many=True)
    #    return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
