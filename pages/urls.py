from django.urls import path
from .views import HomePageView, BasesPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('bases/', BasesPageView.as_view(), name='bases'),
]