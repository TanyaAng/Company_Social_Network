from rest_framework import generics as rest_generic_views, status
from rest_framework import views as rest_views
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import pagination

from datetime import date

from Company_social_network.api_posts.serializers import PostSerializer, LikeSerializer
from Company_social_network.core.repository.api_posts_repository import get_all_posts_not_deleted, find_post_by_pk, \
    get_post, find_is_current_user_has_liked_the_post


class PostPagination(pagination.PageNumberPagination):
    page_size = 20


class ListCreatePostView(rest_generic_views.ListCreateAPIView):
    queryset = get_all_posts_not_deleted()
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DetailsPostView(rest_views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        found_post = find_post_by_pk(pk)
        if not found_post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post = get_post(found_post)
        serializer = PostSerializer(post)
        return Response(data=serializer.data)

    def delete(self, request, pk):
        found_post = find_post_by_pk(pk)
        if not found_post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post = get_post(found_post)
        if not post.author == self.request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post.deleted = True
        post.date_deleted = date.today()
        post.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateLikeView(rest_views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk, *args, **kwargs):
        found_post = find_post_by_pk(pk)
        if not found_post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post = get_post(found_post)
        user = request.user
        post_like = find_is_current_user_has_liked_the_post(post, user)
        if post_like:
            post_like.delete()
            return Response(status=status.HTTP_201_CREATED)
        else:
            serializer = LikeSerializer(post_like, data=request.data, context={'request': request, 'post': post.id})
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
