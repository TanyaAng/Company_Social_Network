from rest_framework import serializers

from Company_social_network.api_posts.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    total_likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'content', 'publication_date_time', 'total_likes')

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
