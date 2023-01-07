from django.contrib.auth import get_user_model

from rest_framework import generics as rest_generic_views, views as rest_views, status
from rest_framework.authtoken import models as authtoken_models
from rest_framework.authtoken import views as authtoken_views
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import exceptions

from Company_social_network.api_auth.models import Profile
from Company_social_network.api_auth.serializers import CreateUserSerializer, LoginUserSerializer, ProfileSerializer

UserModel = get_user_model()


class RegisterApiView(rest_generic_views.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CreateUserSerializer


class LoginApiView(authtoken_views.ObtainAuthToken):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user.is_active:
            token, created = authtoken_models.Token.objects.get_or_create(user=user)

            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email,
            })
        # return Response(status=status.HTTP_401_UNAUTHORIZED)


class LogoutApiView(rest_views.APIView):
    def get(self, request):
        return self.__perform_logout(request)

    def post(self, request):
        return self.__perform_logout(request)

    def __perform_logout(self, request):
        request.user.auth_token.delete()
        return Response(
            {'message': 'user logged out'}
        )


class CreateProfileView(rest_generic_views.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = ProfileSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)


# class DetailsProfileView(rest_generic_views.RetrieveUpdateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     lookup_field = 'pk'
#     permission_classes = (permissions.IsAuthenticated,)
#
#     def get_object(self):
#         profile = super().get_object()
#         if profile.user != self.request.user:
#             raise exceptions.PermissionDenied

class DetailsProfileView(rest_views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        profile = Profile.objects.filter(user_id=pk)
        if not profile:
            return Response(status=status.HTTP_404_NOT_FOUND)
        profile = profile.get()
        if not profile.user == self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = ProfileSerializer(profile)
        return Response(data=serializer.data)

    def put(self, request, pk):
        profile = Profile.objects.filter(user_id=pk)
        if not profile:
            return Response(status=status.HTTP_404_NOT_FOUND)
        profile = profile.get()
        if not profile.user == self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

