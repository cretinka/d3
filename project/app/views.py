from django.shortcuts import render, get_object_or_404, redirect
from .models import NewsArticle
from .forms import NewsArticleForm

def news_list(request):
    articles = NewsArticle.objects.order_by('-date')
    return render(request, 'news/news_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(NewsArticle, pk=article_id)
    return render(request, 'news/article_detail.html', {'article': article})

def add_news(request):
    if request.method == 'POST':
        form = NewsArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsArticleForm()
    return render(request, 'news/add_news.html', {'form': form})
