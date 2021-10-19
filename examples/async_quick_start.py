import asyncio
import getpass
from socialvoidpy import AsyncSocialvoidClient
from socialvoidpy.errors import (
    SessionNotFound,
    SessionDoesNotExist,
    SessionExpired,
    TwoFactorAuthenticationRequired,
)


async def main():
    async with AsyncSocialvoidClient("session.json") as sv:
        authenticated = (await sv.session.get()).authenticated
        if not authenticated:
            username = input("Username: ")
            password = getpass.getpass()
            try:
                await sv.session.authenticate_user(username, password)
            except TwoFactorAuthenticationRequired:
                otp = input("2FA: ")
                await sv.session.authenticate_user(username, password, otp)
        print(await sv.network.get_me())


asyncio.get_event_loop().run_until_complete(main())
