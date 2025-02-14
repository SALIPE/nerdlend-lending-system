from customer_app.models import Customer, CustomerChargeLog, Penalty
from django.contrib.auth.hashers import make_password
from rest_framework import serializers


class CustomerDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['cvid', 'ccname', 'ccemail', 'cvbalance', 'cvcreatedate']
        read_only_fields = ['cvid']


# Serializer for creating/updating customer records
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['cvid', 'ccname', 'ccemail', 'cvbalance']

    def create(self, validated_data):
        customer = Customer.objects.create(**validated_data)
        return customer

    def update(self, instance, validated_data):
        # Update fields
        instance.ccname = validated_data.get('ccname', instance.ccname)
        instance.ccemail = validated_data.get('ccemail', instance.ccemail)
        instance.cvbalance = validated_data.get('cvbalance', instance.cvbalance)
        
        instance.save()
        return instance


# Serializer for customer charge logs
class CustomerChargeLogSerializer(serializers.ModelSerializer):
    cvidcustomer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())

    class Meta:
        model = CustomerChargeLog
        fields = ['cvid', 'cvvalue', 'cvidcustomer', 'cvcreatedate']

    def create(self, validated_data):
        customer = validated_data.pop('cvidcustomer')
        
        charge_log = CustomerChargeLog.objects.create(cvidcustomer=customer, **validated_data)
        return charge_log

    def update(self, instance, validated_data):
        instance.cvvalue = validated_data.get('cvvalue', instance.cvvalue)
        customer = validated_data.get('cvidcustomer')
        if customer:
            instance.cvidcustomer = customer

        instance.save()
        return instance


# Serializer for penalties
class PenaltySerializer(serializers.ModelSerializer):
    class Meta:
        model = Penalty
        fields = ['cvid', 'cvscheduleid', 'cvdaysdelayed', 'cbpayed']
        read_only_fields = ['cvid']

    def create(self, validated_data):
        penalty = Penalty.objects.create(**validated_data)
        return penalty

    def update(self, instance, validated_data):
        instance.cvscheduleid = validated_data.get('cvscheduleid', instance.cvscheduleid)
        instance.cvdaysdelayed = validated_data.get('cvdaysdelayed', instance.cvdaysdelayed)
        instance.cbpayed = validated_data.get('cbpayed', instance.cbpayed)

        instance.save()
        return instance
