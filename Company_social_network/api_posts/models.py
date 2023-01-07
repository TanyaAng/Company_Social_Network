from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Post(models.Model):
    CONTENT_MAX_LENGTH = 400
    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.RESTRICT,
        editable=False,
    )

    content = models.TextField(
        max_length=CONTENT_MAX_LENGTH,
    )

    publication_date_time = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )

    deleted = models.BooleanField(
        default=False,
        null=True,
        blank=True,
    )

    date_deleted = models.DateField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['-publication_date_time']


class Like(models.Model):
    to_post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.RESTRICT,
    )
