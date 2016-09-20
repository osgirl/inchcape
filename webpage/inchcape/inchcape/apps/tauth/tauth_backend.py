import pyotp

from django.contrib.auth.models import User


class TauthBackend:
    """Simple backend for token only authentication."""
    totp = pyotp.TOTP("base64secret3232")

    def authenticate(self, token):
        print(self.totp.now())
        user = User.objects.first()
        if(user):
            return user
        return None
