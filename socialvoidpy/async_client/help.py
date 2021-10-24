import typing
from .. import types
from ..request import Request

if typing.TYPE_CHECKING:
    from . import AsyncSocialvoidClient


class Help:
    """
    `help` methods
    """

    def __init__(self, sv: "AsyncSocialvoidClient"):
        self._sv = sv
        self._cached_server_info = None

    async def get_community_guidelines(self) -> types.HelpDocument:
        """
        Retrieves the community guidelines

        **Returns:** [`types.HelpDocument`](/types/#helpdocument)
        """

        resp = (
            await self._sv.make_request(Request("help.get_community_guidelines"))
        ).unwrap()
        return types.HelpDocument.from_json(resp)

    async def get_privacy_policy(self) -> types.HelpDocument:
        """
        Retrieves the privacy policy

        **Returns:** [`types.HelpDocument`](/types/#helpdocument)
        """

        resp = (
            await self._sv.make_request(Request("help.get_privacy_policy"))
        ).unwrap()
        return types.HelpDocument.from_json(resp)

    async def get_server_information(self) -> types.ServerInformation:
        """
        Retrieves server information, unlike other methods the result is cached

        **Returns:** [`types.ServerInformation`](/types/#serverinformation)
        """

        if not self._cached_server_info:
            resp = (
                await self._sv.make_request(Request("help.get_server_information"))
            ).unwrap()
            self._cached_server_info = types.ServerInformation.from_json(resp)
        return self._cached_server_info

    async def get_terms_of_service(self) -> types.HelpDocument:
        """
        Retrieves the terms of service

        **Returns:** [`types.HelpDocument`](/types/#helpdocument)
        """

        resp = (
            await self._sv.make_request(Request("help.get_terms_of_service"))
        ).unwrap()
        return types.HelpDocument.from_json(resp)
