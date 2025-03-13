from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db import transaction
import logging

from .models import FashionItem
from .serializers import FashionItemSerializer


# Configure logging
logger = logging.getLogger(__name__)


class FashionItemViewSet(viewsets.ModelViewSet):
    queryset = FashionItem.objects.all()
    serializer_class = FashionItemSerializer
    permission_classes = [AllowAny]



    def update(self, request, *args, **kwargs):
        """Handles updating a record (PUT/PATCH)."""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        logger.info(f"Received update request for ID {instance.id} with data: {request.data}")

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            with transaction.atomic():  # Ensure database integrity
                serializer.save()
                logger.info(f"Successfully updated ID {instance.id}")
            return Response(serializer.data)

        logger.error(f"Update failed for ID {instance.id}: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """Handles deleting a record (DELETE)."""
        instance = self.get_object()
        logger.info(f"Received delete request for ID {instance.id}")

        try:
            with transaction.atomic():
                instance.delete()
                logger.info(f"Successfully deleted ID {instance.id}")
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            logger.error(f"Error deleting ID {instance.id}: {str(e)}")
            return Response({"error": "Failed to delete record."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def perform_update(self, serializer):
        """Ensures the update method properly saves changes."""
        serializer.save()

    def perform_destroy(self, instance):

        instance.delete()

    def get_queryset(self):
        """Filters queryset based on pet category if provided in request parameters."""
        queryset = FashionItem.objects.all()
        pet_category = self.request.query_params.get('pet_category')
        if pet_category:
            queryset = queryset.filter(pet_category=pet_category)
        return queryset