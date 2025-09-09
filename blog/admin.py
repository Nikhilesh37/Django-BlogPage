from django.contrib import admin
from .models import Blogs,author,tag,Comment
# Register your models here.
class BlogsAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "slug")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("date",)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")
admin.site.register(Blogs, BlogsAdmin)
admin.site.register(author)
admin.site.register(tag)
admin.site.register(Comment, CommentAdmin)