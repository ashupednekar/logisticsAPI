from django.urls import path
from .views import FeatureView

urlpatterns = [
    path('api/', FeatureView.as_view() )
]