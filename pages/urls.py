from django.urls import path
from .views import BasesPageView

urlpatterns = [
    path('', BasesPageView.as_view(), name='home'),
]