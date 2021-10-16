import typing
from .. import types
from ..utils import async_create_session_id, async_auto_create_session
from ..request import Request

if typing.TYPE_CHECKING:
    from . import AsyncSocialvoidClient


class Account:
    """
    `account` methods
    """

    def __init__(self, sv: "AsyncSocialvoidClient"):
        self._sv = sv

    @async_auto_create_session
    async def delete_profile_picture(self) -> bool:
        """
        Removes the profile picture of the currently logged in account

        **Authentication Required:** Yes
        """

        return (
            await self._sv.make_request(
                Request(
                    "account.delete_profile_picture",
                    {
                        "session_identification": await async_create_session_id(
                            self._sv.session_storage
                        )
                    },
                )
            )
        ).unwrap()

    @async_auto_create_session
    async def set_profile_picture(
        self, document: typing.Union[str, types.Document]
    ) -> bool:
        """
        Sets the profile picture of the currently logged in account

        **Parameters:**

        - **document** (`str`, [`types.Document`](/types/#document)): The photo of the profile picture you want set

        **Authentication Required:** Yes
        """

        if isinstance(document, types.Document):
            document = document.id
        return (
            await self._sv.make_request(
                Request(
                    "account.set_profile_picture",
                    {
                        "session_identification": await async_create_session_id(
                            self._sv.session_storage
                        ),
                        "document": document,
                    },
                )
            )
        ).unwrap()

    @async_auto_create_session
    async def clear_profile_biography(self) -> bool:
        """
        Clears the biography/description of the currently logged in account

        **Authentication Required:** Yes
        """

        return (
            await self._sv.make_request(
                Request(
                    "account.clear_profile_biography",
                    {
                        "session_identification": await async_create_session_id(
                            self._sv.session_storage
                        )
                    },
                )
            )
        ).unwrap()

    @async_auto_create_session
    async def clear_profile_location(self) -> bool:
        """
        Clears the location of the currently logged in account

        **Authentication Required:** Yes
        """

        return (
            await self._sv.make_request(
                Request(
                    "account.clear_profile_location",
                    {
                        "session_identification": await async_create_session_id(
                            self._sv.session_storage
                        )
                    },
                )
            )
        ).unwrap()

    @async_auto_create_session
    async def clear_profile_url(self) -> bool:
        """
        Clears the URL of the currently logged in account

        **Authentication Required:** Yes
        """

        return (
            await self._sv.make_request(
                Request(
                    "account.clear_profile_url",
                    {
                        "session_identification": await async_create_session_id(
                            self._sv.session_storage
                        )
                    },
                )
            )
        ).unwrap()

    @async_auto_create_session
    async def clear_profile_url(self) -> bool:
        """
        Clears the URL of the currently logged in account

        **Authentication Required:** Yes
        """

        return await (
            self._sv.make_request(
                Request(
                    "account.clear_profile_url",
                    {
                        "session_identification": create_session_id(
                            self._sv.session_storage
                        )
                    },
                )
            )
        ).unwrap()

    @async_auto_create_session
    async def update_profile_biography(self, biography: str) -> bool:
        """
        Sets the biography of the currently logged in account

        **Parameters:**

        - **biography** (`str`): The biography you want to set

        **Authentication Required:** Yes
        """

        return await (
            self._sv.make_request(
                Request(
                    "account.update_profile_biography",
                    {
                        "session_identification": create_session_id(
                            self._sv.session_storage
                        ),
                        "biography": biography,
                    },
                )
            )
        ).unwrap()

    @async_auto_create_session
    async def update_profile_location(self, location: str) -> bool:
        """
        Sets the location of the currently logged in account

        **Parameters:**

        - **location** (`str`): The location you want to set

        **Authentication Required:** Yes
        """

        return await (
            self._sv.make_request(
                Request(
                    "account.update_profile_biography",
                    {
                        "session_identification": create_session_id(
                            self._sv.session_storage
                        ),
                        "location": location,
                    },
                )
            )
        ).unwrap()

    @async_auto_create_session
    async def update_profile_name(
        self, first_name: str, last_name: typing.Optional[str] = None
    ) -> bool:
        """
        Sets the first and last name of the currently logged in account

        **Parameters:**

        - **first_name** (`str`): The first name you want to set
        - **last_name** (`str`, `None`, optional): The first name you want to set

        **Authentication Required:** Yes
        """

        params = {
            "session_identification": create_session_id(self._sv.session_storage),
            "first_name": first_name,
        }
        if last_name:
            params["last_name"] = last_name
        return await (
            self._sv.make_request(Request("account.update_profile_name", params))
        ).unwrap()

    @async_auto_create_session
    async def update_profile_url(self, url: str) -> bool:
        """
        Sets the URL of the currently logged in account

        **Parameters:**

        - **url** (`str`): The URL you want to set

        **Authentication Required:** Yes
        """

        return await (
            self._sv.make_request(
                Request(
                    "account.update_profile_url",
                    {
                        "session_identification": create_session_id(
                            self._sv.session_storage
                        ),
                        "url": url,
                    },
                )
            )
        ).unwrap()
