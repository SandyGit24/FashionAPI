from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include

def home(request):
    return JsonResponse({"message": "Welcome to the Fashion API!"})

urlpatterns = [
    path('', home),  # Add this line to handle requests to '/'
    path('admin/', admin.site.urls),
    path('api/', include('fashion_api.urls')),
]
