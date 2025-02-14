# serializers allows us to perform crud operations with high level code
from rest_framework import serializers

from .models import Association, Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

    def create(self, validated_data):
        schedule = Schedule.objects.create(**validated_data)
        return schedule

    def update(self, instance, validated_data):
        # Update fields
        instance.cdwithdrawdate = validated_data.get('cdwithdrawdate', instance.cdwithdrawdate)
        instance.cdduedate = validated_data.get('cdduedate', instance.cdduedate)
        instance.cdreturneddate = validated_data.get('cdreturneddate', instance.cdreturneddate)
        instance.cvvalue = validated_data.get('cvvalue', instance.cvvalue)
        
        instance.save()
        return instance


class AssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Association
        fields = '__all__'

    def create(self, validated_data):
        ass = Association.objects.create(**validated_data)
        return ass
    
class AssociationDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Association
        fields = '__all__'