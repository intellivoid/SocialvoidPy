import json
import typing
import secrets
from .. import types
from ..request import Request
from ..utils import get_platform, create_session_id
from ..version import version

if typing.TYPE_CHECKING:
    from . import AsyncSocialvoidClient


class Session:
    """
    `session` methods and session storage

    See also: [Custom Session Storage](/custom_session_storage)
    """

    def __init__(
        self,
        sv: "AsyncSocialvoidClient",
        public_hash: typing.Optional[str] = None,
        private_hash: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_challenge: typing.Optional[str] = None,
        session_exists: bool = False,
    ):
        self._sv = sv
        self.public_hash = public_hash
        self.private_hash = private_hash
        self.session_id = session_id
        self.session_challenge = session_challenge
        self.session_exists = session_exists

    @classmethod
    def load(cls, sv: "AsyncSocialvoidClient", filename: str):
        with open(filename) as file:
            data = json.load(file)
        return cls(
            sv,
            data.get("public_hash"),
            data.get("private_hash"),
            data.get("session_id"),
            data.get("session_challenge"),
            data.get("session_exists"),
        )

    def save(self, filename: str):
        with open(filename, "w+") as file:
            json.dump(
                {
                    "public_hash": self.public_hash,
                    "private_hash": self.private_hash,
                    "session_id": self.session_id,
                    "session_challenge": self.session_challenge,
                    "session_exists": self.session_exists,
                },
                file,
            )

    async def create(
        self,
        name: str = "SocialvoidPy",
        version: str = version,
        platform: typing.Optional[str] = None,
    ):
        """
        Creates a session

        **Usage:**

        ```python
        >>> await sv.session.create("Fridgevoid", "1.0.1", "Samsung Smart Fridge")
        ```

        **Parameters:**

        - **name** *(optional)*: Name of client
        - **version** *(optional)*: Version of client
        - **platform** *(optional)*: Platform of client
        """

        if platform is None:
            platform = get_platform()
        self.public_hash = public_hash = secrets.token_hex(32)
        self.private_hash = private_hash = secrets.token_hex(32)
        resp = (
            await self._sv.make_request(
                Request(
                    "session.create",
                    {
                        "public_hash": public_hash,
                        "private_hash": private_hash,
                        "name": name,
                        "version": version,
                        "platform": platform,
                    },
                )
            )
        ).unwrap()
        self.session_id = resp["id"]
        self.session_challenge = resp["challenge"]
        self.session_exists = True
        self._sv._save_session()

    async def get(self) -> types.Session:
        """
        Gets information about the current session

        **Returns:** [`types.Session`](/types/#Session)
        """

        return types.Session.from_json(
            (
                await self._sv.make_request(
                    Request(
                        "session.get",
                        {"session_identification": create_session_id(self)},
                    )
                )
            ).unwrap()
        )

    async def logout(self) -> None:
        """
        Logs out of the account associated to the session, or does nothing if not logged in
        """

        await self._sv.make_request(
            Request(
                "session.logout",
                {"session_identification": create_session_id(self)},
                notification=True,
            )
        )

    async def authenticate_user(
        self, username: str, password: str, otp: typing.Optional[str] = None
    ) -> bool:
        """
        Logs in to an account

        **Usage:**

        ```python
        >>> await sv.session.authenticate_user("blankie", "i need some sleep")
        ```

        **Parameters:**

        - **username**: Username of the account to login to
        - **password**: Password of the account to login to
        - **otp** *(optional)*: Optional One-Time Password of the account to login to
        """

        params = {
            "session_identification": create_session_id(self),
            "username": username,
            "password": password,
        }
        if otp is not None:
            params["otp"] = otp
        return (
            await self._sv.make_request(Request("session.authenticate_user", params))
        ).unwrap()

    async def register(
        self,
        terms_of_service_id: str,
        username: str,
        password: str,
        first_name: str,
        last_name: typing.Optional[str] = None,
    ) -> types.Peer:
        """
        Registers an account

        **Usage:**

        ```python
        >>> await sv.session.register("idhere", "blankie", "i need some sleep", "blankies", "blankets")
        # TODO return output
        ```

        **Parameters:**

        - **terms_of_service_id**: Terms of Service ID from [`help.get_terms_of_service`](#help)
        - **username**: Username of the account
        - **password**: Password of the account
        - **first_name**: First name of the account
        - **last_name** *(optional)*: Last name of the account

        **Returns:** The [`types.Peer`](/types/#peer) of the new account
        """

        params = {
            "session_identification": create_session_id(self),
            "terms_of_service_id": terms_of_service_id,
            "terms_of_service_agree": True,
            "username": username,
            "password": password,
            "first_name": first_name,
            "last_name": last_name,
        }
        return types.Peer.from_json(
            (await self._sv.make_request(Request("session.register", params))).unwrap()
        )
