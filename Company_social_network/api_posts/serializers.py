from rest_framework import serializers

from Company_social_network.api_posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'content', 'publication_date_time')

    def create(self, validated_data):
        # print(self.context['user'])
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
