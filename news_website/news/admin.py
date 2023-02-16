from django.contrib import admin

from .models import News, Group


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'body',
        'image',
        'author',
        'group',
        'publish_date'
    )
    list_editable = ('group',)
    search_fields = ('title',)
    list_filter = ('publish_date',)
    empty_value_display = '-пусто-'


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
