from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_pagination, name='news_pagination'),
    path('create', views.news_create, name='news_create'),
    path('<int:pk>', views.NewsDetailView.as_view(), name='news_details'),
    path('<int:pk>/update', views.NewsUpdateView.as_view(), name='news_update')
    # path('pagination/', views.news_pagination, name='news_pagination')
]