import typing
from .. import types
from ..request import Request


class Help:
    def __init__(self, sv: "AsyncSocialvoidClient"):
        self._sv = sv

    async def get_community_guidelines(self) -> types.HelpDocument:
        resp = (
            await self._sv.make_request(Request("help.get_community_guidelines"))
        ).unwrap()
        return types.HelpDocument.from_json(resp)

    async def get_privacy_policy(self) -> types.HelpDocument:
        resp = (
            await self._sv.make_request(Request("help.get_privacy_policy"))
        ).unwrap()
        return types.HelpDocument.from_json(resp)

    async def get_server_information(self) -> types.ServerInformation:
        resp = (
            await self._sv.make_request(Request("help.get_server_information"))
        ).unwrap()
        return types.ServerInformation.from_json(resp)

    async def get_terms_of_service(self) -> types.HelpDocument:
        resp = (
            await self._sv.make_request(Request("help.get_terms_of_service"))
        ).unwrap()
        return types.HelpDocument.from_json(resp)
