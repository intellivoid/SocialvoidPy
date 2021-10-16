import typing
import secrets
from .. import types
from ..request import Request
from ..utils import get_platform, create_session_id
from ..version import version

if typing.TYPE_CHECKING:
    from . import SocialvoidClient


class Session:
    """
    `session` methods and session storage

    See also: [Custom Session Storage](/custom_session_storage)
    """

    def __init__(
        self,
        sv: "SocialvoidClient",
    ):
        self._sv = sv

    def create(
        self,
        name: str = "SocialvoidPy",
        version: str = version,
        platform: typing.Optional[str] = None,
    ):
        """
        Creates a session

        **Usage:**

        ```python
        >>> sv.session.create("Fridgevoid", "1.0.1", "Samsung Smart Fridge")
        ```

        **Parameters:**

        - **name** (`str`, optional): Name of client
        - **version** (`str`, optional): Version of client
        - **platform** (`str`, `None`, optional): Platform of client

        **Session Required:** No (it literally makes one)
        """

        if platform is None:
            platform = get_platform()
        public_hash = secrets.token_hex(32)
        private_hash = secrets.token_hex(32)
        resp = self._sv.make_request(
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
        ).unwrap()
        self._sv.session_storage.set_public_hash(public_hash)
        self._sv.session_storage.set_private_hash(private_hash)
        self._sv.session_storage.set_session_id(resp["id"])
        self._sv.session_storage.set_session_challenge(resp["challenge"])
        self._sv.session_storage.flush()

    def get(self) -> types.Session:
        """
        Gets information about the current session

        **Returns:** [`types.Session`](/types/#Session)

        **Session Required:** Yes
        """

        return types.Session.from_json(
            self._sv.make_request(
                Request(
                    "session.get",
                    {
                        "session_identification": create_session_id(
                            self._sv.session_storage
                        )
                    },
                )
            ).unwrap()
        )

    def logout(self) -> None:
        """
        Logs out of the account associated to the session, or does nothing if not logged in

        **Session Required:** Yes
        """

        self._sv.make_request(
            Request(
                "session.logout",
                {"session_identification": create_session_id(self._sv.session_storage)},
                notification=True,
            )
        )

    def authenticate_user(
        self, username: str, password: str, otp: typing.Optional[str] = None
    ) -> bool:
        """
        Logs in to an account

        **Usage:**

        ```python
        >>> sv.session.authenticate_user("blankie", "i need some sleep")
        ```

        **Parameters:**

        - **username** (`str`): Username of the account to login to
        - **password** (`str`): Password of the account to login to
        - **otp** (`str`, `None`, optional): Optional One-Time Password of the account to login to

        **Session Required:** Yes
        """

        params = {
            "session_identification": create_session_id(self._sv.session_storage),
            "username": username,
            "password": password,
        }
        if otp is not None:
            params["otp"] = otp
        return self._sv.make_request(
            Request("session.authenticate_user", params)
        ).unwrap()

    def register(
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
        >>> sv.session.register("idhere", "blankie", "i need some sleep", "blankies", "blankets")
        Peer(id='f65e2f25e1bfbf876ba865a41f71d93833b37c5c3c75e827bc2bb1da45bd7962', type=<PeerType.USER: 'USER'>, name='blankies blankets', username='blankie', display_picture_sizes=[], flags=[])
        ```

        **Parameters:**

        - **terms_of_service_id** (`str`): Terms of Service ID from [`help.get_terms_of_service`](#help)
        - **username** (`str`): Username of the account
        - **password** (`str`): Password of the account
        - **first_name** (`str`): First name of the account
        - **last_name** (`str`, `None`, optional): Last name of the account

        **Returns:** The [`types.Peer`](/types/#peer) of the new account

        **Session Required:** Yes
        """

        params = {
            "session_identification": create_session_id(self._sv.session_storage),
            "terms_of_service_id": terms_of_service_id,
            "terms_of_service_agree": True,
            "username": username,
            "password": password,
            "first_name": first_name,
            "last_name": last_name,
        }
        return types.Peer.from_json(
            self._sv.make_request(Request("session.register", params)).unwrap()
        )
