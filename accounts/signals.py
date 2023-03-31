from django.contrib.auth.signals import user_logged_in, user_registered
from django.dispatch import receiver
from .models import UserProfile

@receiver(user_logged_in)
@receiver(user_registered)
def create_user_profile(sender, user, request, **kwargs):
    if not hasattr(user, 'userprofile'):
        profile = UserProfile.objects.create(user=user)
        profile.save()
