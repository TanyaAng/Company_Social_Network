from django.urls import path, include

from Company_social_network.api_posts.views import ListCreatePostView, DetailsPostView, CreateLikeView

urlpatterns = (
    path('', ListCreatePostView.as_view(), name='api list posts'),
    path('<int:pk>/',
         include([
             path('', DetailsPostView.as_view(), name='api detail post'),
             path('like/', CreateLikeView.as_view(), name='api create like')
         ])
         )
)
