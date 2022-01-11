from django.contrib import admin
from .models import Article, Comments


# visualize 2 two model in a single page.


class CommentInLine(admin.TabularInline):
    model = Comments


class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comments) # SHOULD HAVE BEEN IN SINGULAR!!



