from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import ArticleListView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleDetailView

app_name = 'stock'

urlpatterns = [
    path('', login_required(ArticleListView.as_view()), name='article_list'),
    path('add/', login_required(ArticleCreateView.as_view()), name='article_add'),
    path('view/<int:pk>/', login_required(ArticleDetailView.as_view()), name='article_detail'),
    path('change/<int:pk>/', login_required(ArticleUpdateView.as_view()), name='article_change'),
    path('delete/<int:pk>/', login_required(ArticleDeleteView.as_view()), name='article_delete'),
]
