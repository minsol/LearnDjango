from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    # # ex: /myapp/
    # path('', views.index, name='index'),
    # # ex: /myapp/current_datetime/
    # path('current_datetime', views.current_datetime, name='current_datetime'),
    # # ex: /myapp/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /myapp/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /myapp/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # 注意，第二个和第三个匹配准则中，路径字符串中匹配模式的名称已经由 <question_id> 改为 <pk>。
    
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]