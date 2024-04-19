from django.contrib import admin
from .models import Post, Customization, Image, Attachment, Comment, Tag, Article, ArticleComment

admin.site.register(Post)
admin.site.register(Customization)
admin.site.register(Image)
admin.site.register(Attachment)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Article)
admin.site.register(ArticleComment)