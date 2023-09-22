from django.urls import path
from .views import CombinedApiView

urlpatterns = [
  path('combined/', CombinedApiView.as_view()),
]