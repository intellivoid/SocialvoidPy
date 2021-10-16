import typing
import secrets
from .. import types
from ..request import Request
from ..utils import async_create_session_id, async_auto_create_session, maybe_await
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
    ):
        self._sv = sv

    async def create(
        self,
        name: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        platform: typing.Optional[str] = None,
    ):
        """
        Creates a session

        **Usage:**

        ```python
        >>> await sv.session.create("Fridgevoid", "1.0.1", "Samsung Smart Fridge")
        ```

        **Parameters:**

        - **name** (`str`, optional): The name of the client, defaults to `SocialvoidClient.client_name`
        - **version** (`str`, optional): The version of the client, defaults to `SocialvoidClient.client_version`
        - **platform** (`str`, `None`, optional): The platform of the client, defaults to `SocialvoidClient.client_platform`
        """

        if name is None:
            name = self._sv.client_name
        if version is None:
            version = self._sv.client_version
        if platform is None:
            platform = self._sv.client_platform
        public_hash = secrets.token_hex(32)
        private_hash = secrets.token_hex(32)
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
        await maybe_await(self._sv.session_storage.set_public_hash(public_hash))
        await maybe_await(self._sv.session_storage.set_private_hash(private_hash))
        await maybe_await(self._sv.session_storage.set_session_id(resp["id"]))
        await maybe_await(
            self._sv.session_storage.set_session_challenge(resp["challenge"])
        )
        await maybe_await(self._sv.session_storage.flush())

    @async_auto_create_session
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
                        {
                            "session_identification": await async_create_session_id(
                                self._sv.session_storage
                            )
                        },
                    )
                )
            ).unwrap()
        )

    @async_auto_create_session
    async def logout(self) -> None:
        """
        Logs out of the account associated to the session, or does nothing if not logged in
        """

        await self._sv.make_request(
            Request(
                "session.logout",
                {
                    "session_identification": await async_create_session_id(
                        self._sv.session_storage
                    )
                },
                notification=True,
            )
        )

    @async_auto_create_session
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

        - **username** (`str`): Username of the account to login to
        - **password** (`str`): Password of the account to login to
        - **otp** (`str`, `None`, optional): Optional One-Time Password of the account to login to
        """

        params = {
            "session_identification": await async_create_session_id(
                self._sv.session_storage
            ),
            "username": username,
            "password": password,
        }
        if otp is not None:
            params["otp"] = otp
        return (
            await self._sv.make_request(Request("session.authenticate_user", params))
        ).unwrap()

    @async_auto_create_session
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
        Peer(id='f65e2f25e1bfbf876ba865a41f71d93833b37c5c3c75e827bc2bb1da45bd7962', type=<PeerType.USER: 'USER'>, name='blankies blankets', username='blankie', display_picture_sizes=[], flags=[])
        ```

        **Parameters:**

        - **terms_of_service_id** (`str`): Terms of Service ID from [`help.get_terms_of_service`](#help)
        - **username** (`str`): Username of the account
        - **password** (`str`): Password of the account
        - **first_name** (`str`): First name of the account
        - **last_name** (`str`, `None`, optional): Last name of the account

        **Returns:** The [`types.Peer`](/types/#peer) of the new account
        """

        params = {
            "session_identification": await async_create_session_id(
                self._sv.session_storage
            ),
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
