from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from news.models import Tag, Category, News, Comments


class NewsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text', 'text_min')


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(News, NewsAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'created', 'moderation')     # отображение в админке


admin.site.register(Comments, CommentAdmin)
