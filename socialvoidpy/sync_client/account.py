import typing
from .. import types
from ..utils import create_session_id
from ..request import Request


class Account:
    def __init__(self, sv: "SocialvoidClient"):
        self._sv = sv

    def delete_profile_picture(self) -> bool:
        return self._sv.make_request(
            Request(
                "account.delete_profile_picture",
                {"session_identification": create_session_id(self._sv.session)},
            )
        ).unwrap()

    def set_profile_picture(self, document: typing.Union[str, types.Document]) -> bool:
        if isinstance(document, types.Document):
            document = document.id
        return self._sv.make_request(
            Request(
                "account.set_profile_picture",
                {
                    "session_identification": create_session_id(self._sv.session),
                    "document": document,
                },
            )
        ).unwrap()
