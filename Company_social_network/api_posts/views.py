from rest_framework import generics as rest_generic_views, status
from rest_framework import views as rest_views
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import pagination

from datetime import date

from Company_social_network.api_posts.models import Post, Like
from Company_social_network.api_posts.serializers import PostSerializer, LikeSerializer


class PostPagination(pagination.PageNumberPagination):
    page_size = 20


class ListCreatePostView(rest_generic_views.ListCreateAPIView):
    queryset = Post.objects.filter(deleted=False)
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class DetailsPostView(rest_views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        post = Post.objects.filter(id=pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post = post.get()
        serializer = PostSerializer(post)
        return Response(data=serializer.data)

    def delete(self, request, pk):
        post = Post.objects.filter(id=pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post = post.get()
        if not post.author == self.request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post.deleted = True
        post.date_deleted = date.today()
        post.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class CreateLikeView(rest_generic_views.CreateAPIView):
#     queryset = Like.objects.all()
#     serializer_class = LikeSerializer
#     permission_classes = (permissions.IsAuthenticated,)

class CreateLikeView(rest_views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.filter(id=pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post = post.get()
        post_like = Like.objects.filter(to_post_id=post, user_id=request.user).first()
        if post_like:
            post_like.delete()
            return Response(status=status.HTTP_201_CREATED)
        else:
            serializer = LikeSerializer(post_like, data=request.data, context={'request': request, 'post': post.id})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
