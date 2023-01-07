from django.urls import path

from Company_social_network.api_posts.views import ListCreatePostView, DetailsPostView

urlpatterns = (
    path('', ListCreatePostView.as_view(), name='api list posts'),
    path('<int:pk>/', DetailsPostView.as_view(), name='api detail post'),
)
