from django.shortcuts import render
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles_data':articles})


def article_detail(request,slug):
    #return HttpResponse(slug)
    article_slug  = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article_slug})

#@login_required(login_url="/accounts/login")
def article_create(request):
    return render(request, 'articles/article_create.html')
