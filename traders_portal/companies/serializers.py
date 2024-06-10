from rest_framework import serializers

from .models import Company, Watchlist


class CompanySerializer(serializers.ModelSerializer):
    symbol = serializers.CharField(required=False)
    scripcode = serializers.CharField(required=False)
    
    class Meta:
        model = Company
        fields = '__all__'
        
    def validate_scripcode(self, value):
        if not value.isdigit() or len(value) < 6 or len(value) > 6:
            raise serializers.ValidationError("Invalid scripcode")
        return value
    
    def validate_symbol(self, value):
        if not value.isupper():
            raise serializers.ValidationError("Invalid symbol")
        return value

class WatchlistSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    
    class Meta:
        model = Watchlist
        fields = ['company']
