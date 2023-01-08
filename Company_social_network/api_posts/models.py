from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

UserModel = get_user_model()


class Post(models.Model):
    CONTENT_MAX_LENGTH = 400
    SECONDS_IN_A_DAY = 24 * 60 * 60
    SECONDS_IN_A_HOUR = 1 * 60 * 60
    SECONDS_IN_A_MINUTE = 60
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

    @property
    def time_diff(self):
        now = timezone.now()
        start = self.publication_date_time
        diff = now - start
        if diff.seconds > self.SECONDS_IN_A_DAY:
            return f"{diff.seconds // self.SECONDS_IN_A_DAY}d"
        if diff.seconds > self.SECONDS_IN_A_HOUR:
            return f"{diff.seconds // self.SECONDS_IN_A_HOUR}h"
        if diff.seconds > self.SECONDS_IN_A_MINUTE:
            return f"{diff.seconds // self.SECONDS_IN_A_MINUTE}min"
        return f"now"


class Like(models.Model):
    to_post = models.ForeignKey(
        to=Post,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.RESTRICT,
    )
