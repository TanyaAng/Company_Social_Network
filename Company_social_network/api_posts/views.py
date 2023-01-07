from rest_framework import generics as rest_generic_views, status
from rest_framework import views as rest_views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import pagination



from datetime import date

from Company_social_network.api_posts.models import Post
from Company_social_network.api_posts.serializers import PostSerializer


class PostPagination(pagination.PageNumberPagination):
    page_size = 20


class ListCreatePostView(rest_generic_views.ListCreateAPIView):
    queryset = Post.objects.filter(deleted=False)
    serializer_class = PostSerializer
    pagination_class = PostPagination
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=self.request.user)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class DetailsPostView(rest_views.APIView):
    permission_classes = (IsAuthenticated,)

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
        post.deleted = True
        post.date_deleted = date.today()
        post.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
