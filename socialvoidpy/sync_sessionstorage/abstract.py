import typing
from abc import ABC, abstractmethod

# if get_public_hash, get_private_hash, get_session_id or get_session_challenge returns None, the session does not exist
class AbstractSessionStorage(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_public_hash(self) -> typing.Optional[str]:
        """
        Gets the session's public hash if any

        **Returns:** `str` or `None`
        """

        raise NotImplementedError

    @abstractmethod
    def get_private_hash(self) -> typing.Optional[str]:
        """
        Gets the session's private hash if any

        **Returns:** `str` or `None`
        """

        raise NotImplementedError

    @abstractmethod
    def get_session_id(self) -> typing.Optional[str]:
        """
        Gets the session ID if any

        **Returns:** `str` or `None`
        """

        raise NotImplementedError

    @abstractmethod
    def get_session_challenge(self) -> typing.Optional[str]:
        """
        Gets the session challenge if any

        **Returns:** `str` or `None`
        """

        raise NotImplementedError

    @abstractmethod
    def set_public_hash(self, public_hash: str):
        """
        Sets the session's public hash

        **Parameters:**

        - **public_hash** (`str`): The session's public hash
        """

        raise NotImplementedError

    @abstractmethod
    def set_private_hash(self, private_hash: str):
        """
        Sets the session's private hash

        **Parameters:**

        - **private_hash** (`str`): The session's private hash
        """

        raise NotImplementedError

    @abstractmethod
    def set_session_id(self, session_id: str):
        """
        Sets the session ID

        **Parameters:**

        - **session_id** (`str`): The session ID
        """

        raise NotImplementedError

    @abstractmethod
    def set_session_challenge(self, session_challenge: str):
        """
        Sets the session challenge

        **Parameters:**

        - **session_challenge** (`str`): The session challenge
        """

        raise NotImplementedError

    @abstractmethod
    def close(self):
        """
        Closes any stuff like active connections if any
        """

        raise NotImplementedError

    @abstractmethod
    def flush(self):
        """
        Called when important data needs to be saved
        """

        raise NotImplementedError
