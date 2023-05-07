from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

# Create a custom authentication backend that authenticates users using their email address
UserModel = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            # Looks up the users by email
            user = UserModel.objects.get(Q(email__exact=email))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return None
        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(Q(email__exact=email)).order_by('id').first()

        # Check if the user's password matches the given password, and if the user can authenticate
        if user.check_password(password) and self.user_can_authenticate(user):
            return user