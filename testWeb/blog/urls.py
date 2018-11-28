from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search', views.search, name='search'),
    path('aboutMe', views.aboutMe, name='aboutMe'),
    path('detail', views.detail, name='detail'),
]