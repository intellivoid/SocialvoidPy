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

    async def get_community_guidelines(self) -> types.HelpDocument:
        """
        Retrieves the community guidelines

        **Returns:** [`types.HelpDocument`](/types/#helpdocument)

        **Session Required:** No
        """

        resp = (
            await self._sv.make_request(Request("help.get_community_guidelines"))
        ).unwrap()
        return types.HelpDocument.from_json(resp)

    async def get_privacy_policy(self) -> types.HelpDocument:
        """
        Retrieves the privacy policy

        **Returns:** [`types.HelpDocument`](/types/#helpdocument)

        **Session Required:** No
        """

        resp = (
            await self._sv.make_request(Request("help.get_privacy_policy"))
        ).unwrap()
        return types.HelpDocument.from_json(resp)

    async def get_server_information(self) -> types.ServerInformation:
        """
        Retrieves server information

        **Returns:** [`types.ServerInformation`](/types/#serverinformation)

        **Session Required:** No
        """

        resp = (
            await self._sv.make_request(Request("help.get_server_information"))
        ).unwrap()
        return types.ServerInformation.from_json(resp)

    async def get_terms_of_service(self) -> types.HelpDocument:
        """
        Retrieves the terms of service

        **Returns:** [`types.HelpDocument`](/types/#helpdocument)

        **Session Required:** No
        """

        resp = (
            await self._sv.make_request(Request("help.get_terms_of_service"))
        ).unwrap()
        return types.HelpDocument.from_json(resp)
