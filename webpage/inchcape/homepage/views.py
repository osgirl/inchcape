from pyotp import TOTP

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if(token_valid(request)):
        return HttpResponse('This is the secret page')
    else:
        return HttpResponse('This is the home page')


def token_valid(request):
    totp = TOTP("longpassword2")

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
