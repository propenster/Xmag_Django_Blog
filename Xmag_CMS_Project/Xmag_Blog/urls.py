from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='article_list'),
    # path('posts', views.home, name='home'),
    path('<int:pk>', views.article_detail, name='article_detail'),
]
