from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['sequence', 'title']
    prepopulated_fields = {'slug': ('title',)}