from django.contrib import admin

from Company_social_network.api_posts.models import Post, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'publication_date_time', 'deleted', 'date_deleted')
    ordering = ('-publication_date_time',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('to_post', 'user')

# # @admin.register(MyCronJob)
# class MyCronJobAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(MyCronJob, MyCronJobAdmin)
