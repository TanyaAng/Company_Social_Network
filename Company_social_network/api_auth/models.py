from django.contrib.auth import models as auth_models
from django.db import models

from Company_social_network.api_auth.managers import CompanyUserManager
from Company_social_network.core.validators.model_validators import only_letters_validator, \
    max_file_size_validator_to_5MB


class CompanyUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    date_joined = models.DateTimeField(auto_now_add=True)

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=False,
    )

    objects = CompanyUserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 40
    DESCRIPTION_MAX_LENGTH = 150

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(only_letters_validator,),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(only_letters_validator,),
    )

    profile_picture = models.ImageField(
        upload_to='user_profile_pictures/',
        validators=(max_file_size_validator_to_5MB,),
        null=True,
        blank=True,
    )

    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        CompanyUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


