import typing
from .. import types
from ..utils import create_session_id
from ..request import Request

if typing.TYPE_CHECKING:
    from . import SocialvoidClient


class Cloud:
    """
    `cloud` methods
    """

    def __init__(self, sv: "SocialvoidClient"):
        self._sv = sv

    def get_document(
        self, document: typing.Union[str, types.Document]
    ) -> types.Document:
        """
        Gets a document from a document's ID

        **Parameters:**

        - **document**: A document ID

        **Returns:** [`types.Document`](/types/#document)

        **Authentication Required:** Yes (for now?)
        """

        # no idea why you want to refetch a document but it is what it is
        if isinstance(document, types.Document):
            document = document.id
        return types.Document.from_json(
            self._sv.make_request(
                Request(
                    "cloud.get_document",
                    {
                        "session_identification": create_session_id(self._sv.session),
                        "document": document,
                    },
                )
            ).unwrap()
        )
