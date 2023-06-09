from django.contrib import admin

from .models import Post, Author, Tag

class PostAdmin(admin.ModelAdmin):
    list_filter = ("autor","tag","date",)
    list_display = ("title","date","autor",)
    prepopulated_fields = {"slug" : ("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)

