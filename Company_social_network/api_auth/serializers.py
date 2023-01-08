from rest_framework import serializers

from django.contrib.auth import get_user_model, password_validation, authenticate
from django.core import exceptions

from django.utils.translation import gettext_lazy as _

from Company_social_network.api_auth.models import Profile
from Company_social_network.api_posts.models import Post, Like

UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'password')

        # This hashes the password (Not save in plain-text in the DB)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(user.password)
        user.save()
        return user

    def validate(self, data):
        # Invoke password validators
        user = UserModel(**data)
        password = data.get('password')
        errors = {}
        try:
            password_validation.validate_password(password, user)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)
        if errors:
            raise serializers.ValidationError(errors)
        return super().validate(data)

    def to_representation(self, instance):
        user_representation = super().to_representation(instance)
        user_representation.pop('password')
        return user_representation


class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email"),
        # style={'input_type': 'email'},
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class ProfileSerializer(serializers.ModelSerializer):
    total_posts = serializers.SerializerMethodField(read_only=True)
    total_likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'profile_picture', 'description', 'total_posts', 'total_likes')

    def create(self, validated_data):
        print(self.context['request'].user)
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def get_total_posts(self, profile: Profile):
        user = profile.user
        total_count_of_user_posts = Post.objects.filter(author_id=user).count()
        return total_count_of_user_posts

    def get_total_likes(self, profile: Profile):
        user = profile.user
        total_posts_of_user = Post.objects.filter(author_id=user)
        total_likes = 0
        for post in total_posts_of_user:
            total_likes += Like.objects.filter(to_post_id=post).count()
        return total_likes


