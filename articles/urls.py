from django.urls import path
from .views import ArticlesListView, ArticlesCreateView, ArticlesDeleteView, ArticlesUpdateView, ArticlesDetailView

urlpatterns = [
    path('edit/<int:pk>/', ArticlesUpdateView.as_view(), name='articles_edit'),
    path('new/', ArticlesCreateView.as_view(), name='articles_new'),
    path('<int:pk>/', ArticlesDetailView.as_view(), name='articles_detail'),
    path('delete/<int:pk>/', ArticlesDeleteView.as_view(), name='articles_delete'),
    path('', ArticlesListView.as_view(), name='articles_list'),
]