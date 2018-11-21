from django.urls import path
from . import views

urlpatterns = [
    # ex: /myapp/
    path('index', views.index, name='index'),
    # ex: /myapp/current_datetime/
    path('current_datetime', views.current_datetime, name='current_datetime'),
    # ex: /myapp/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /myapp/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /myapp/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]