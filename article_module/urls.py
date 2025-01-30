from django.urls import path
from . import views
urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article'),
    path('cat/<str:category>', views.ArticleListView.as_view(), name='article_categorise'),
    path('<pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('comments', views.article_comments, name='article_comments')
]