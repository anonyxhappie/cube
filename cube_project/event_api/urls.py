from django.urls import include, path
from .views import TriggerEventView

urlpatterns = [
    path('trigger/', TriggerEventView.as_view())
]
