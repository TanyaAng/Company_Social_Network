from django.urls import path, include

from Company_social_network.api_auth.views import RegisterApiView, LoginApiView, LogoutApiView, DetailsProfileView, \
    CreateProfileView

urlpatterns = (
    path('register/', RegisterApiView.as_view(), name='api register user'),
    path('login/', LoginApiView.as_view(), name='api login'),
    path('logout/', LogoutApiView.as_view(), name='api logout'),
    path('profile/',
         include([
             path('', CreateProfileView.as_view(), name='api create profile'),
             path('<int:pk>/', DetailsProfileView.as_view(), name='api details profile'),
         ])
         )
)
