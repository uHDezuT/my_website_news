from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'news'

urlpatterns = [
    path('', views.main, name='main'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )