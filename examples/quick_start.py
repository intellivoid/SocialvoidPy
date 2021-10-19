import getpass
from socialvoidpy import SocialvoidClient
from socialvoidpy.errors import (
    SessionNotFound,
    SessionDoesNotExist,
    SessionExpired,
    TwoFactorAuthenticationRequired,
)

with SocialvoidClient("session.json") as sv:
    authenticated = sv.session.get().authenticated
    if not authenticated:
        username = input("Username: ")
        password = getpass.getpass()
        try:
            sv.session.authenticate_user(username, password)
        except TwoFactorAuthenticationRequired:
            otp = input("2FA: ")
            sv.session.authenticate_user(username, password, otp)
    print(sv.network.get_me())
