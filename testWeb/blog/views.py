from django.shortcuts import render
from django.views import View
from .models import Blog

class IndexView(View):
    # 首页
    def get(self, request):
        all_blog = Blog.objects.order_by('-create_time')[:5]
        return render(request, 'index.html', {
            'all_blog': all_blog,
        })

#配置404 500错误页面
def page_not_found(request):
    return render(request, '404.html')

def page_errors(request):
    return render(request, '500.html')

def search(request):
    return render(request, 'search.html')

def aboutMe(request):
    return render(request, 'aboutMe.html')
    # return render(request, 'portfolio/aboutMe.html')

def detail(request):
    return render(request, 'blog.html')
    