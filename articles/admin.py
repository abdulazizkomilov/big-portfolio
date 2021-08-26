from django.contrib import admin
from .models import Articles, Comment
# Register your models here.

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class ArticlesAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]

admin.site.register(Articles, ArticlesAdmin)
admin.site.register(Comment)