from pyotp import TOTP


class MedRecordMiddleware:
    def process_request(self, request):
        totp = TOTP("longpassword2")
        valid_totp = totp.now()

        print("Middleware exicuted")
        print(dir(request))

        raw_payload = request.read()
        # Load the payload into a dictionary.
        try:
            payload = dict(item.split("=") for item in raw_payload.decode('utf8').split("&"))
            print(payload)

            if(valid_totp.verify(payload['token'])):
            # if(valid_totp.verify(payload['token']) == valid_totp):
                print("OK")
                print(payload['token'])
                print(valid_totp)

            else:
                print("NOT OK")

        except Exception as e:
            print(e)
