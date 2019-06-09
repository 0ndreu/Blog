from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from news.models import Tag, Category, News, Comments


class NewsAdmin(SummernoteModelAdmin):
    """
    в поле, где применяется ForeignKey или ManyToMany, надо явное указание поля, по которому надо искать
    """
    list_display = ('title', 'user', 'created')
    list_editable = ('user', )          # редактировать поле прямо при выводе статей в админке
    summernote_fields = ('text', 'text_min')
    list_filter = ('user', 'created', )
    search_fields = ['title', 'user__username']     # инструкция в начале


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'new', 'created', 'moderation')     # порядок отображения в админке


admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentAdmin)
