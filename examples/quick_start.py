import getpass
from socialvoidpy import (
    SocialvoidClient,
    SessionExpired,
    TwoFactorAuthenticationRequired,
)

sv = SocialvoidClient("session.json")
try:
    if not sv.session.session_exists:
        sv.session.create()
    try:
        authenticated = sv.session.get().authenticated
    except SessionExpired:
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
