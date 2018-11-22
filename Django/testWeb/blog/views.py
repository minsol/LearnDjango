from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def search(request):
    return render(request, 'search.html')

def aboutMe(request):
    return render(request, 'aboutMe.html')
    # return render(request, 'portfolio/aboutMe.html')
    