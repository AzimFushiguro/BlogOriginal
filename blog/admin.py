from django.contrib import admin
from blog.models import Posts,Category
from django.contrib.auth.models import Group, User
admin.site.unregister(Group)
admin.site.unregister(User)
@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ("id","title","created_at")
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","title")
# Register your models here.
