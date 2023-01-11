from collections.abc import Generator
from typing import Any

from openpyxl.descriptors.serialisable import Serialisable

RESERVED: Any
RESERVED_REGEX: Any
COL_RANGE: str
COL_RANGE_RE: Any
ROW_RANGE: str
ROW_RANGE_RE: Any
TITLES_REGEX: Any

class DefinedName(Serialisable):
    tagname: str
    name: str
    comment: str | None
    customMenu: str | None
    description: str | None
    help: str | None
    statusBar: str | None
    localSheetId: int | None
    hidden: bool | None
    function: bool | None
    vbProcedure: bool | None
    xlm: bool | None
    functionGroupId: int | None
    shortcutKey: str | None
    publishToServer: bool | None
    workbookParameter: bool | None
    attr_text: Any
    value: Any
    def __init__(
        self,
        name: str = ...,
        comment: str | None = ...,
        customMenu: str | None = ...,
        description: str | None = ...,
        help: str | None = ...,
        statusBar: str | None = ...,
        localSheetId: int | None = ...,
        hidden: bool | None = ...,
        function: bool | None = ...,
        vbProcedure: bool | None = ...,
        xlm: bool | None = ...,
        functionGroupId: int | None = ...,
        shortcutKey: str | None = ...,
        publishToServer: bool | None = ...,
        workbookParameter: bool | None = ...,
        attr_text: Any | None = ...,
    ) -> None: ...
    @property
    def type(self): ...
    @property
    def destinations(self) -> Generator[Any, None, None]: ...
    @property
    def is_reserved(self): ...
    @property
    def is_external(self): ...
    def __iter__(self): ...

class DefinedNameList(Serialisable):
    tagname: str
    definedName: Any
    def __init__(self, definedName=...) -> None: ...
    def append(self, defn: DefinedName) -> None: ...
    def __len__(self) -> int: ...
    def __contains__(self, name: str): ...
    def __getitem__(self, name: str): ...
    def get(self, name, scope: Any | None = ...): ...
    def __delitem__(self, name: str) -> None: ...
    def delete(self, name, scope: Any | None = ...): ...
    def localnames(self, scope): ...
