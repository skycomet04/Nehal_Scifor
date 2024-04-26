from .models import StockData
from rest_framework import serializers

class viewDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=StockData
        fields=['stock_sym','stockprice']