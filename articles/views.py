from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from .import forms
from django.contrib.auth.decorators import login_required

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles_data':articles})


def article_detail(request,slug):
    #return HttpResponse(slug)
    article_slug  = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article_slug})

@login_required(login_url="/accounts/login")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
