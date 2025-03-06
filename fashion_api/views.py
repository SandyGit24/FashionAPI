from rest_framework import viewsets
from .models import FashionItem
from .serializers import FashionItemSerializer

class FashionItemViewSet(viewsets.ModelViewSet):
    queryset = FashionItem.objects.all()
    serializer_class = FashionItemSerializer
