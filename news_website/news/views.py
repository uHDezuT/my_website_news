from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .models import News

SELECT_LIMIT = 10  # лимит постов на странице


def paginator(request, news):
    paginate = Paginator(news, SELECT_LIMIT)
    page_number = request.GET.get('page')
    page = paginate.get_page(page_number)
    return page


def main(request):
    """Главная страница сайта."""

    news = News.objects.all()
    page = paginator(request, news)
    context = {
        'page_obj': page,
    }
    return render(request, 'news/main.html', context)


def news_detail(request, news_id):
    """Страница с описанием поста."""
    user_news = get_object_or_404(News, id=news_id)
    author = user_news.author
    publish_date = user_news.publish_date
    news_count = user_news.author.news.count()
    context = {
        'news_count': news_count,
        'user_news': user_news,
        'author': author,
        'publish_date': publish_date,
    }
    return render(request, 'news/news_detail.html', context)
