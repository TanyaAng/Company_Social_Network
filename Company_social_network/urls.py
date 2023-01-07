from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('Company_social_network.api_auth.urls')),
    path('posts/', include('Company_social_network.api_posts.urls')),
]
