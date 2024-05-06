from rest_framework import serializers
from firstApp.models import Vender_Model,PO_Model,Performance_Model

class VenderSerializers(serializers.ModelSerializer):
    class Meta:
        model=Vender_Model
        fields=['name','contact_details','address','vender_code']

class POSerializer(serializers.ModelSerializer):
    class Meta:
        model=PO_Model
        fields='__all__'

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Performance_Model
        fields='__all__'