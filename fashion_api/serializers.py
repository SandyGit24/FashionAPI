from rest_framework import serializers
from .models import FashionItem

class FashionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FashionItem
        fields = '__all__'
