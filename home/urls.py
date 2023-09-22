from django.urls import path
from .views import CombinedApiView

urlpatterns = [
  path('', CombinedApiView.as_view()),
]