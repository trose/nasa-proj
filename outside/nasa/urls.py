from django.urls import path 
from .views import (
    MediaView,
)

urlpatterns = [
    path('apod', MediaView.as_view()),
]