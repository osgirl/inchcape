from pyotp import TOTP

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .forms import TOTPForm


@csrf_exempt
def index(request):
    if(request.method == 'GET'):
        return homepage(request)

    if(request.method == 'POST' and 'token' in request.POST):
        print('Token in POST')
        form = TOTPForm(request.POST)
        print('form')
        print(form)
        if(form.is_valid()):
            if(token_valid(request)):
                return protected_page(request)
            else:
                return homepage(request)


@csrf_exempt
def protected_page(request):
    print('med_record called')
    return HttpResponse('This is the secret page')


def homepage(request):
    print('homepage called')
    return HttpResponse('This is the home page')


def token_valid(request):
    totp = TOTP("longpassword2")

    raw_payload = request.read()
    try:
        # Load the payload into a dictionary.
        payload = dict(item.split("=") for item in raw_payload.decode('utf8').split("&"))

        if(totp.verify(payload['token'])):
            return True
        # else:
            # return False

    except Exception as e:
        print(e)
    else:
        return False
