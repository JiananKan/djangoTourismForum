from django.contrib import admin
from travels.models import UserProfile, Article, Comment


# Register your models here.

# superuser -u admin -p a123456789

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publish_date')
    prepopulated_fields = {'slug': ('title',)}


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'user', 'picture')


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
