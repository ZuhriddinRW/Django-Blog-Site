from django.contrib import admin
from .models import Article


class ArticleAdmin ( admin.ModelAdmin ) :
    list_display = ['title', 'author', 'id']
    fields = ['title', 'summary', 'body', 'photo']

    def save_model(self, request, obj, form, change) :
        if not change :
            obj.author = request.user
        super ().save_model ( request, obj, form, change )


admin.site.register ( Article, ArticleAdmin )