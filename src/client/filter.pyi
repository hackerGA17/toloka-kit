from enum import Enum
from typing import Any, Dict, List, Optional, Union

from .primitives.base import BaseTolokaObject
from .primitives.operators import (
    ComparableConditionMixin,
    CompareOperator,
    IdentityConditionMixin,
    IdentityOperator,
    InclusionConditionMixin,
    InclusionOperator,
    StatefulComparableConditionMixin
)


class FilterCondition(BaseTolokaObject):

    def __or__(self, other: 'FilterCondition'): ...

    def __and__(self, other: 'FilterCondition'): ...

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

class FilterOr(FilterCondition):

    def __or__(self, other: FilterCondition): ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, or_: List[FilterCondition]) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    or_: List[FilterCondition]

class FilterAnd(FilterCondition):

    def __and__(self, other): ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, and_: List[FilterCondition]) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    and_: List[FilterCondition]

class Condition(FilterCondition):

    class Category(Enum):
        ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, operator: Any, value: Any) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: Any
    value: Any

class Profile(Condition):

    class Key(Enum):
        ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, operator: Any, value: Any) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: Any
    value: Any

class Computed(Condition):

    class Key(Enum):
        ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, *, operator: Any, value: Any) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: Any
    value: Any

class Skill(StatefulComparableConditionMixin, Condition):

    def __repr__(self): ...

    def __str__(self): ...

    def __init__(
        self,
        key: str,
        operator: CompareOperator = ...,
        value: Optional[float] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    key: str
    operator: CompareOperator
    value: Optional[float]

class Gender(Profile, IdentityConditionMixin):

    class Gender(Enum):
        ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: IdentityOperator, value: Gender) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: IdentityOperator
    value: Gender

class Country(Profile, IdentityConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: IdentityOperator, value: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: IdentityOperator
    value: str

class Citizenship(Profile, IdentityConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: IdentityOperator, value: str) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: IdentityOperator
    value: str

class Education(Profile, IdentityConditionMixin):

    class Education(Enum):
        ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: IdentityOperator, value: Education) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: IdentityOperator
    value: Education

class AdultAllowed(Profile, IdentityConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: IdentityOperator, value: bool) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: IdentityOperator
    value: bool

class DateOfBirth(Profile, ComparableConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: CompareOperator, value: int) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: int

class City(Profile, InclusionConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: InclusionOperator, value: int) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: InclusionOperator
    value: int

class Languages(Profile, InclusionConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: InclusionOperator,
        value: Union[str, List[str]]
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: InclusionOperator
    value: Union[str, List[str]]

class RegionByPhone(Computed, InclusionConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: InclusionOperator, value: int) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: InclusionOperator
    value: int

class RegionByIp(Computed, InclusionConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: InclusionOperator, value: int) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: InclusionOperator
    value: int

class DeviceCategory(Computed, IdentityConditionMixin):

    class DeviceCategory(Enum):
        ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: IdentityOperator, value: DeviceCategory) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: IdentityOperator
    value: DeviceCategory

class ClientType(Computed, IdentityConditionMixin):

    class ClientType(Enum):
        ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: IdentityOperator, value: ClientType) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: IdentityOperator
    value: ClientType

class OSFamily(Computed, IdentityConditionMixin):

    class OSFamily(Enum):
        ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: IdentityOperator, value: OSFamily) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: IdentityOperator
    value: OSFamily

class OSVersion(Computed, ComparableConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: CompareOperator, value: float) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: float

class OSVersionMajor(Computed, ComparableConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: CompareOperator, value: int) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: int

class OSVersionMinor(Computed, ComparableConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: CompareOperator, value: int) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: int

class OSVersionBugfix(Computed, ComparableConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: CompareOperator, value: int) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: int

class UserAgentType(Computed, IdentityConditionMixin):

    class UserAgentType(Enum):
        ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: IdentityOperator, value: UserAgentType) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: IdentityOperator
    value: UserAgentType

class UserAgentFamily(Computed, IdentityConditionMixin):

    class UserAgentFamily(Enum):
        ...

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(self, operator: IdentityOperator, value: UserAgentFamily) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: IdentityOperator
    value: UserAgentFamily

class UserAgentVersion(Computed, ComparableConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[float]

class UserAgentVersionMajor(Computed, ComparableConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[int]

class UserAgentVersionMinor(Computed, ComparableConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[int]

class UserAgentVersionBugfix(Computed, ComparableConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[int] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[int]

class Rating(Computed, ComparableConditionMixin):

    def __repr__(self): ...

    def __str__(self): ...

    def __eq__(self, other): ...

    def __ne__(self, other): ...

    def __lt__(self, other): ...

    def __le__(self, other): ...

    def __gt__(self, other): ...

    def __ge__(self, other): ...

    def __init__(
        self,
        operator: CompareOperator,
        value: Optional[float] = ...
    ) -> None: ...

    _unexpected: Optional[Dict[str, Any]]
    operator: CompareOperator
    value: Optional[float]