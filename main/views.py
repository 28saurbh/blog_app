from django.shortcuts import render
from .models import CreateBlog
from django.db.models import Q
from django.shortcuts import redirect

# Create your views here.


def index(request):
    blog_data = CreateBlog.objects.all().order_by('-pub_date')
    return render(request, 'index.html', {'data': blog_data})

def all_docs(request):
    data = CreateBlog.objects.all().order_by('-pub_date')
    return render(request, 'all_docs.html',{'data': data})

# All category Documentations like-django-html-css
def cat_docs(request):
    return render(request, 'cat_docs.html')
    
    
def blog(request, slug):
    blog_data = CreateBlog.objects.filter(slug = slug)  
    return render(request, 'blog.html', {'data':blog_data[0]})


# category Blogs like-django_blogs
def cat_blog(request):
    cat_blog_data = CreateBlog.objects.filter(cat = 'Django')
    return render(request, 'cat_blog.html',{'data':cat_blog_data})


# Search Result
def search(request):
    query = request.GET.get('search')
    object_list = CreateBlog.objects.filter(Q(title__icontains=query) | Q(cat__icontains=query))
    return render(request, 'search.html',{'data':object_list, 'query':query})