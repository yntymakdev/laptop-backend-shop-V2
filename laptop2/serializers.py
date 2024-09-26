from rest_framework import serializers
from .models import *


class LaptopPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LaptopPhoto
        fields = '__all__'


class LaptopSerializer(serializers.ModelSerializer):
    laptop = LaptopPhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Laptop
        fields = ['brand','model','processor','ram_size','storage_size','laptop','price','description']
