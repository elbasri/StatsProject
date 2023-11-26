from rest_framework import serializers
from .models import Statsprj

class StatsprjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statsprj
        fields = '__all__'
