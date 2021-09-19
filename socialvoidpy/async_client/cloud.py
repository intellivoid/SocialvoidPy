import typing
from .. import types
from ..utils import create_session_id
from ..request import Request


class Cloud:
    def __init__(self, sv: "AsyncSocialvoidClient"):
        self._sv = sv

    async def get_document(
        self, document: typing.Union[str, types.Document]
    ) -> types.Document:
        # no idea why you want to refetch a document but it is what it is
        if isinstance(document, types.Document):
            document = document.id
        return types.Document.from_json(
            (
                await self._sv.make_request(
                    Request(
                        "cloud.get_document",
                        {
                            "session_identification": create_session_id(
                                self._sv.session
                            ),
                            "document": document,
                        },
                    )
                )
            ).unwrap()
        )
