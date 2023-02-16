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
