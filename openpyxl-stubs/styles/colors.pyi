from openpyxl.descriptors.serialisable import Serialisable
from openpyxl.drawing.colors import SystemColor
from typing import (
    Iterator,
    List,
    Optional,
    Tuple,
    Union,
)

class Color:
    def __add__(self, other: Union[Color, int]) -> Color: ...
    def __init__(
        self,
        rgb: str = ...,
        indexed: Optional[Union[str, int]] = ...,
        auto: Optional[Union[str, bool, int]] = ...,
        theme: Optional[Union[str, int]] = ...,
        tint: Union[float, str] = ...,
        index: None = ...,
        type: str = ...,
    ) -> None: ...
    def __iter__(self) -> Iterator[Tuple[str, str]]: ...
    @property
    def index(self) -> int: ...

class ColorDescriptor:
    def __set__(
        self, instance: Serialisable, value: Optional[Union[str, Color]]
    ) -> None: ...

class ColorList:
    def __bool__(self) -> bool: ...
    def __init__(
        self,
        indexedColors: Union[
            Tuple[str, str],
            List[str],
            Tuple,
            List[RgbColor],
            Tuple[
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
                str,
            ],
        ] = ...,
        mruColors: Union[List[Color], Tuple] = ...,
    ) -> None: ...
    @property
    def index(self) -> List[str]: ...

class RGB:
    def __set__(
        self,
        instance: Union[Color, SystemColor, RgbColor],
        value: Optional[Union[str, int]],
    ) -> None: ...

class RgbColor:
    def __init__(self, rgb: Optional[str] = ...) -> None: ...
