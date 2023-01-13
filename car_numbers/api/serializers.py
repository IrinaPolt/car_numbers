import re
from django.contrib.auth import get_user_model
from rest_framework import serializers

from plates.models import Plate

User = get_user_model()

PLATE_FORMAT = re.compile(r'^[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}(?P<reg>\d{2,3})$') # можно вывести регион и сортировать по регионам в дальнейшем


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
        fields = ('number', )
    
    def validate(self, data):
        if PLATE_FORMAT.match(data):
            return data
        else:
            raise serializers.ValidationError('Введенный номер не соответствует стандарту')
