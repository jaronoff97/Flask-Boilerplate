from oauth2client import client, crypt
from flask import request, abort

# (Receive token by HTTPS POST)

# put this in for example gauth.py
CLIENT_ID = "914337337536-p90o02ch5fuef72q3pmkhvjqnke241\
pa.apps.googleusercontent.com"
ANDROID_CLIENT_ID = ""
IOS_CLIENT_ID = "914337337536-b1qh140d4j435btnd228lue0bp\
8rosgp.apps.googleusercontent.com"
WEB_CLIENT_ID = ""
APPS_DOMAIN_NAME = ""


def validate_token(token):
    '''Verifies that an access-token is valid and
    meant for this app.

    Returns None on fail, and an e-mail on success'''
    try:
        idinfo = client.verify_id_token(token, CLIENT_ID)
        # If multiple clients access the backend server:
        if idinfo['aud\
        '] not in [ANDROID_CLIENT_ID, IOS_CLIENT_ID, WEB_CLIENT_ID]:
            raise crypt.AppIdentityError("Unrecognized client.")
        if idinfo['iss'] not in ['accounts.google.com\
        ', 'https://accounts.google.com']:
            raise crypt.AppIdentityError("Wrong issuer.")
        if idinfo['hd'] != APPS_DOMAIN_NAME:
            raise crypt.AppIdentityError("Wrong hosted domain.")
    except crypt.AppIdentityError:
        print "NOT WORKING"
        # Invalid token
    userid = idinfo['sub']
    return userid


def authorized(fn):
    """Decorator that checks that requests
    contain an id-token in the request header.
    userid will be None if the
    authentication failed, and have an id otherwise.

    Usage:
    @app.route("/")
    @authorized
    def secured_root(userid=None):
        pass
    """

    def _wrap(*args, **kwargs):
        if 'Authorization' not in request.headers:
            # Unauthorized
            print("No token in header")
            abort(401)
            return None

        print("Checking token...")
        userid = validate_token(request.headers['Authorization'])
        if userid is None:
            print("Check returned FAIL!")
            # Unauthorized
            abort(401)
            return None

        return fn(userid=userid, *args, **kwargs)
    return _wrap
