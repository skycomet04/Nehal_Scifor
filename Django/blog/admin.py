from django.contrib import admin
from blog.models import Contact,Blog,Comment
# Register your models here.
admin.site.register(Contact)
admin.site.register(Comment)
class BlogAdmin(admin.ModelAdmin):
    list_display=["title","updated"]
    list_filter=["updated","title"]

    class Meta:
        model= Blog
admin.site.register(Blog)
