from pyotp import TOTP

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from .models import MedRecord
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
                return med_record(request)
            else:
                return homepage(request)


@csrf_exempt
def med_record(request):
    print('med_record called')
    return render(request, 'medrecord/record.html')


def homepage(request):
    print('homepage called')
    return HttpResponse('This is the home page')


def token_valid(request):
    totp = TOTP("longpassword2")
    valid_totp = totp.now()

    raw_payload = request.read()
    try:
        # Load the payload into a dictionary.
        payload = dict(item.split("=") for item in raw_payload.decode('utf8').split("&"))

        if(payload['token'] == valid_totp):
            return True
        # else:
            # return False

    except Exception as e:
        print(e)
    else:
        return False
