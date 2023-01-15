import re
import gosnomer
from django.contrib.auth import get_user_model
from rest_framework import serializers

from plates.models import Plate

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class PlateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Plate
        fields = ('plate', )
    
    def validate(self, data):
        number = data['plate']
        number = gosnomer.normalize(number)

        """
        Gosnomer исправляет ручной ввод автомобильных номеров по стандарту РФ.
        Существует список допустимых букв, латиница исправляется на кириллицу.
        В случае ввода недопустимого значения выбрасывается ValueError.
        """

        data['plate'] = number
        return data
