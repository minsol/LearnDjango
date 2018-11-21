---
title: [0002]创建 Django 项目
tags: 
notebook: 【1000】Python
---

### 创建一个 Django 应用 ：testWeb
1. 查找到 pip 安装的 django-admin 位置：/Library/Frameworks/Python.framework/Versions/3.5/bin/django-admin
2. 使用 django-admin 创建项目： django-admin startproject testWeb
3. 运行： python3 manage.py runserver

默认情况下，runserver 命令在 8000 端口启动开发服务器，且仅监听本地连接。要想要更改服务器端口的话，可将端口作为命令行参数传入: python3 manage.py runserver 8080

#### 项目介绍
1. 与项目同名的 testWeb 里面放着的是配置文件
    - __init__.py :让 Python 把该目录当成一个开发包 (即一组模块)所需的文件。 这是一个空文件，一般你 不需要修改它。
    - settings.py :该 Django 项目的设置或配置。 查看并理解这个文件中可用的设置类型及其默认值。
    - urls.py : Django 项目的URL设置。 可视其为你的 django 网站的目录。目前，它是空的。
    - wsgi.py :网络通信接口,作为你的项目的运行在 WSGI 兼容的 Web 服务器上的入口。
2. templates 目录存放 html 文件，也是 MTV 架构中的 T
3. manage.py : Django 管理主程序一种命令行工具，允许你以多种方式与该 Django 项目进行交互。 键入python manage.py help，看一下它能做什么。 你应当不需要编辑这个文件;在这个目录下生成它纯是 为了方便。


### 创建一个应用 : myapp
> 在每个 django 项目中可以包含多个 APP，你可以把 APP 理解为一个大型项目中的分系统、子模块、功能部件等等，相互之间比较独立，但也有联系,所有的 APP 共享项目资源.
<br>项目和应用有啥区别:应用是一个专门做某件事的网络应用程序——比如博客系统，或者公共记录的数据库，或者简单的投票程序。项目则是一个网站使用的配置和应用的集合。项目可以包含很多个应用。应用可以被很多个项目使用。
#### 创建一个名为myapp的APP模块：python manage.py startapp myapp
1. 在项目的下方有一个terminal终端入口，输入一下命令,创建一个名为myapp的APP模块：python manage.py startapp myapp

#### 在 testWeb 里编写路由
在前面我们有介绍 Djang o的架构，里面有一个 urls.py，路由都在urls文件里，它将浏览器输入的url映射到相应的业务处理逻辑。
1. 在 urls.py 里面导入views：from myapp import views
2. 编写路由规则：修改urlpatterns：path('index', views.index),
这个的意思就是当网址路径输入index的时候，展示views.index的界面
> testWeb/urls.py
```python
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index', views.index),
]
```
3. 或者使用incloud()------强烈推荐
何时使用 include():当包括其它 URL 模式时你应该总是使用 include()，admin.site.urls 是唯一例外。
  - 在 myapp 里面创建一个 urls.py
  - 在testWeb里面通过incloud引入
> myapp/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    #路由地址http://127.0.0.1:8000/myapp
    # ex: /myapp/
    path('', views.index, name='index'),
    
    # ex: /myapp/index/
    # path('index', views.index, name='index'),
]
```
> testWeb/urls.py
```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('myapp/', include('myapp.urls')),#在这里引入myapp应用的路由配置
    path('admin/', admin.site.urls),
]
```

#### 在myapp里面编写业务逻辑
上个步骤我们有引用myapp里面的 views.py，但是我们的业务逻辑还没写，需要在views.py写入业务逻辑
> myapp/views.py
```python3
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello Django")
```

### 运行 python3 manage.py runserver
```
http://127.0.0.1:8000/myapp
```

### 数据库配置
#### 创建需要的数据表：python3 manage.py migrate
这个 migrate 命令检查 INSTALLED_APPS 设置，为其中的每个应用创建需要的数据表，至于具体会创建什么，这取决于你的 testWeb/settings.py 设置文件和每个应用的数据库迁移文件。
> testWeb/settings.py
```python
INSTALLED_APPS = [
    'myapp.apps.MyappConfig',# 把 myapp 应用安装到我们的项目里
    'django.contrib.admin',#-- 管理员站点， 你很快就会使用它。
    'django.contrib.auth',#-- 认证授权系统。
    'django.contrib.contenttypes',# -- 内容类型框架。
    'django.contrib.sessions',#-- 会话框架。
    'django.contrib.messages',#-- 消息框架。
    'django.contrib.staticfiles',#-- 管理静态文件的框架
]
#数据库设置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',#可选值有 'django.db.backends.sqlite3'，'django.db.backends.postgresql'，'django.db.backends.mysql'，或 'django.db.backends.oracle'。
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),#数据库的名称。
    }
}

```

#### 创建模型
> myapp/models.py
```python
from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
```

#### 激活模型：python3 manage.py makemigrations myapp
通过运行 makemigrations 命令，Django 会检测你对模型文件的修改（在这种情况下，你已经取得了新的），并且把修改的部分储存为一次迁移。它被储存在 myapp/migrations/0001_initial.py 里。

#### 自动执行数据库迁移并同步管理你的数据库结构： python manage.py sqlmigrate polls 0001
sqlmigrate 命令接收一个迁移的名称，然后返回对应的 SQL：

#### 现在，你只需要记住，改变模型需要这三步：
- 编辑 models.py 文件，改变模型。
- 运行 python3 manage.py makemigrations 为模型的改变生成迁移文件。
- 运行 python3 manage.py migrate 来应用数据库迁移。

### 介绍 Django 管理界面
#### 创建一个管理员账号
首先，我们得创建一个能登录管理页面的用户。请运行下面的命令：
```
python manage.py createsuperuser
```
然后是用户名、邮箱、密码
#### 登录
打开"http://127.0.0.1:8000/admin/" 。你应该会看见管理员登录界面：
#### 向管理页面中加入投票应用
打开 myapp/admin.py 文件，在里面注册我们需要的模型,然后就可以在管理界面对模型进行管理。
> myapp/admin.py
```python
from django.contrib import admin
from .models import Question
# Register your models here.
admin.site.register(Question)
```
接下来就可以在管理界面看到MYAPP-Question这个选项进行管理了。

### 编写跟多的视图
首先，在你的 myapp 目录里创建一个 templates 目录。Django 将会在这个目录里查找模板文件。

#### 创建index.html 用于显示问题的列表
在你刚刚创建的 templates 目录里，再创建一个目录 myapp index.html 。换句话说，你的模板文件的路径应该是 myapp/templates/myapp/index.html 。因为 Django 会寻找到对应的 app_directories ，所以你只需要使用 myapp/index.html 就可以引用到这一模板了。
>myapp/templates/myapp/index.html 
```html
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/myapp/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```
添加业务逻辑
>myapp/views.py
```python
from django.shortcuts import render
from django.shortcuts import HttpResponse
import datetime

from .models import Question

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('myapp/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}#index.html 的参数
    return render(request, 'myapp/index.html', context)
    # render(必须：用于生成此响应的请求对象,必须：要使用的模板的全名或模板名称的序列,可选：要添加到模板上下文的值的字典,)
```
上述代码的作用是，载入 myapp/index.html 模板文件，并且向它传递一个上下文(context)。这个上下文是一个字典，它将模板内的变量映射为 Python 对象。

#### 创建 detail.html 用于显示问题的详情
在你刚刚创建的 templates 目录里，再创建一个目录 myapp detail.html 
> myapp/templates/myapp/detail.html
```html
<h1>{{ question.question_text }}</h1>
<ul>
{% for choice in question.choice_set.all %}
    <li>{{ choice.choice_text }}</li>
{% endfor %}
</ul>
```
添加业务逻辑
>myapp/views.py 
```python
from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponse
import datetime

from .models import Question

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
    
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'myapp/detail.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'myapp/detail.html', {'question': question})

    # get_object_or_404(必选：klass，必选：**kwargs)
    # question = Question。.objects.get(pk=question_id)
```
这时就可以在http://127.0.0.1:8000/myapp/index里面点击问题跳转到问题详情界面。

#### 去除模板中的硬编码 URL
我们在 myapp/templates/myapp/index.html 里编写投票链接时，链接是硬编码的。
然而，因为你在 polls.urls 的 url() 函数中通过 name 参数为 URL 定义了名字，你可以使用 {% url %} 标签代替它
> myapp/templates/myapp/index.html 
```html
 <li><a href="/myapp/{{ question.id }}/">{{ question.question_text }}</a></li>

<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```
#### 为 URL 名称添加命名空间
在根 URLconf 中添加命名空间。在 myapp/urls.py 文件中稍作修改，加上 app_name 设置命名空间：
> myapp/urls.py
```python
from django.urls import path
from . import views

app_name = 'myapp' # 设置命名空间
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
```
>myapp/templates/myapp/index.html 
```html
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```
