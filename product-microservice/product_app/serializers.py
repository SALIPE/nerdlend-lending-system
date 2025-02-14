# product_app/serializers.py
from rest_framework import serializers

from .models import Tbfavorite, Tbproduct


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbproduct
        fields = ['cvid', 'ccdescription', 'ccproducttype'] 
        
class TbproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tbproduct
        fields = ['cvid', 'ccdescription', 'cvamount', 'ccproducttype'] 
        read_only_fields = ['cvid']

    def create(self, validated_data):
        return Tbproduct.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.ccdescription = validated_data.get('ccdescription', instance.ccdescription)
        instance.cvamount = validated_data.get('cvamount', instance.cvamount)
        instance.ccproducttype = validated_data.get('ccproducttype', instance.ccproducttype)
        instance.save()
        return instance

class TbfavoriteSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Tbproduct.objects.all())

    class Meta:
        model = Tbfavorite
        fields = ['cvid', 'cdperiod', 'product']
        read_only_fields = ['cvid']

    def create(self, validated_data):
        return Tbfavorite.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.cdperiod = validated_data.get('cdperiod', instance.cdperiod)
        instance.product = validated_data.get('product', instance.product)
        instance.save()
        return instance