from typing import Any, Dict, Optional

from .base import BaseTolokaObject


class Parameters(BaseTolokaObject):

    def unstructure(self) -> dict: ...

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