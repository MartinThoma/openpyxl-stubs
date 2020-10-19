from lxml.etree import _Element
from openpyxl.styles.colors import Color
from typing import (
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
)

def _assign_position(
    values: Union[List[Color], List[Stop], Tuple, List[Union[Stop, str]], List[str]]
) -> List[Stop]: ...

class Fill:
    @classmethod
    def from_tree(cls, el: _Element) -> Optional[Union[GradientFill, PatternFill]]: ...

class GradientFill:
    def __init__(
        self,
        type: str = ...,
        degree: Union[str, int] = ...,
        left: Union[str, int] = ...,
        right: Union[str, int] = ...,
        top: Union[str, int] = ...,
        bottom: Union[str, int] = ...,
        stop: Union[List[Stop], Tuple] = ...,
    ) -> None: ...
    def __iter__(self) -> Iterator[Tuple[str, str]]: ...
    def to_tree(
        self, tagname: None = ..., namespace: None = ..., idx: None = ...
    ) -> _Element: ...

class PatternFill:
    def __init__(
        self,
        patternType: Optional[str] = ...,
        fgColor: Union[str, Color] = ...,
        bgColor: Union[str, Color] = ...,
        fill_type: Optional[str] = ...,
        start_color: Optional[Union[str, Color]] = ...,
        end_color: Optional[Union[str, Color]] = ...,
    ) -> None: ...
    @classmethod
    def _from_tree(cls, el: _Element) -> PatternFill: ...
    def to_tree(self, tagname: Optional[str] = ..., idx: None = ...) -> _Element: ...

class Stop:
    def __init__(
        self, color: Union[str, Color], position: Optional[Union[float, str, int]]
    ) -> None: ...

class StopList:
    def __set__(self, obj: GradientFill, values: Union[List[Stop], Tuple]) -> None: ...
