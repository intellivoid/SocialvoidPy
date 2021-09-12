import abc

class BaseClass(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def from_json(cls, resp):
        raise NotImplementedError
