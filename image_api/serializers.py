from rest_framework import serializers
from .models import ImagesTable


class ImagesTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesTable
        fields = '__all__'