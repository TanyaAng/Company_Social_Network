from rest_framework import serializers

from Company_social_network.api_posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','author', 'content', 'publication_date_time')



