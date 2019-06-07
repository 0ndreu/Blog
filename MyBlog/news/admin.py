from django.contrib import admin

# Register your models here.
from news.models import Tag, Category, News

admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(News)

