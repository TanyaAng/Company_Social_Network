from django.contrib.auth import get_user_model

from Company_social_network.api_auth.models import Profile

UserModel = get_user_model()


def get_all_users():
    return UserModel.objects.all()

def get_all_profiles():
    return Profile.objects.all()


def find_profile_by_pk(pk):
    return Profile.objects.filter(user_id=pk)


def get_profile(profile):
    return profile.get()
