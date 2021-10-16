import getpass
from socialvoidpy import SocialvoidClient
from socialvoidpy.errors import (
    SessionNotFound,
    SessionDoesNotExist,
    SessionExpired,
    TwoFactorAuthenticationRequired,
)

sv = SocialvoidClient("session.json")
try:
    try:
        authenticated = sv.session.get().authenticated
    except (SessionNotFound, SessionDoesNotExist, SessionExpired):
        sv.session.create()
        authenticated = False
    if not authenticated:
        username = input("Username: ")
        password = getpass.getpass()
        try:
            sv.session.authenticate_user(username, password)
        except TwoFactorAuthenticationRequired:
            otp = input("2FA: ")
            sv.session.authenticate_user(username, password, otp)
    print(sv.network.get_me())
finally:
    sv.close()
