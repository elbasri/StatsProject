from rest_framework import serializers
from .models import UploadedFile, Result, Statsprj

class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['id', 'file', 'uploaded_at', 'parsed_data']

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'

class StatsprjSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statsprj
        fields = '__all__'