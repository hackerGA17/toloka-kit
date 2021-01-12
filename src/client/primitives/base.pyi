from enum import Enum
from typing import Any, Dict, Optional, Type, TypeVar


E = TypeVar('E', bound=Enum)

class VariantRegistry(object):

    def __init__(self, field: str, enum: Type[E]): ...

    def register(self, type_: type, value: E) -> type: ...

    def __getitem__(self, value: E): ...

def attribute(*args, required=..., origin=..., **kwargs): ...

class BaseTolokaObjectMetaclass(type):
    ...

class BaseTolokaObject(object):

    def __getattr__(self, item): ...

    def unstructure(self) -> Optional[dict]: ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self) -> None: ...

    _unexpected: Optional[Dict[str, Any]]