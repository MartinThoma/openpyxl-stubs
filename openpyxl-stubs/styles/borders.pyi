from openpyxl.styles.colors import Color
from typing import (
    Iterator,
    Optional,
    Tuple,
    Union,
)

class Border:
    def __init__(
        self,
        left: Side = ...,
        right: Side = ...,
        top: Side = ...,
        bottom: Side = ...,
        diagonal: Side = ...,
        diagonal_direction: None = ...,
        vertical: None = ...,
        horizontal: None = ...,
        diagonalUp: Union[str, bool] = ...,
        diagonalDown: Union[str, bool] = ...,
        outline: bool = ...,
        start: None = ...,
        end: None = ...,
    ) -> None: ...
    def __iter__(self) -> Iterator[Tuple[str, str]]: ...

class Side:
    def __init__(
        self,
        style: Optional[str] = ...,
        color: Optional[Union[Color, str]] = ...,
        border_style: Optional[str] = ...,
    ) -> None: ...
