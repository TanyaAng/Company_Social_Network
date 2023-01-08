from rest_framework import serializers

from Company_social_network.api_auth.serializers import ExtendedUserSerializer
from Company_social_network.api_posts.models import Post, Like


class ShortPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('publication_date_time',)


class PostSerializer(serializers.ModelSerializer):
    author = ExtendedUserSerializer(read_only=True)
    total_likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'content', 'time_diff', 'total_likes')

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

    def get_total_likes(self, post: Post):
        total_likes = Like.objects.filter(to_post_id=post).count()
        return total_likes


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ()

    def create(self, validated_data):
        validated_data['to_post_id'] = self.context['post']
        validated_data['user_id'] = self.context['request'].user.id
        return super().create(validated_data)
