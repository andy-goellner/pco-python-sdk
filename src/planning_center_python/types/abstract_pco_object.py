from abc import ABC
from typing import Any


class AbstractPCOObject(ABC):
    def __init__(self) -> None:
        raise NotADirectoryError

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        raise NotImplementedError

    def get_attribute(self, name: str) -> Any:
        raise NotImplementedError

    def _object_url(self) -> str:
        raise NotImplementedError

    def _instance_url(self) -> str:
        raise NotImplementedError

    def _validate(self) -> None:
        raise NotImplementedError

    @property
    def id(self) -> str | None:
        raise NotImplementedError

    @property
    def type(self) -> str | None:
        raise NotImplementedError
