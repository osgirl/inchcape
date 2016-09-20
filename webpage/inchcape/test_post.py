from pyotp import TOTP
import requests


def run(token, outfile):
    print('running')
    payload = {'token': token}
    r = requests.post('http://127.0.0.1:8000/', payload)
    print(r.status_code)
    with open(outfile, 'w') as f:
        f.write(r.text)

if(__name__ == '__main__'):
    totp = TOTP("longpassword2")
    run(totp.now(), 'success.html')
    run('666666', 'fail.html')
    run('', 'empty.html')
