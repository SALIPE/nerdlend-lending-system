# serializers allows us to perform crud operations with high level code
from rest_framework import serializers
from .models import Trigger

class TriggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trigger
        fields = '__all__'
