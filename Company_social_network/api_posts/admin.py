from django.contrib import admin

from Company_social_network.api_posts.models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass
