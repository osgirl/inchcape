from pyotp import TOTP

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if(token_valid(request, "longpassword2")):
        return HttpResponse('This is the secret page')
    else:
        return HttpResponse('This is the home page')


def token_valid(request, secret_key):
    totp = TOTP(secret_key)

    try:
        if(request.method == 'POST' and 'token' in request.POST):
            # Load the payload into a dictionary.
            raw_payload = request.read()
            payload = dict(item.split("=") for item in raw_payload.decode('utf8').split("&"))

            if(totp.verify(payload['token'])):
                return True

    except Exception as e:
        print(e)
    else:
        return False
