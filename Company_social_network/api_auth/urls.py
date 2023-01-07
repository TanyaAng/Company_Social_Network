from django.urls import path

from Company_social_network.api_auth.views import RegisterApiView, LoginApiView, LogoutApiView

urlpatterns = (
    path('register/', RegisterApiView.as_view(), name='api register user'),
    path('login/', LoginApiView.as_view(), name='api login'),
    path('logout/', LogoutApiView.as_view(), name='api logout'),
)
