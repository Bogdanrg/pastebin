from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetKeyRequest(_message.Message):
    __slots__ = ("secret",)
    SECRET_FIELD_NUMBER: _ClassVar[int]
    secret: str
    def __init__(self, secret: _Optional[str] = ...) -> None: ...

class GetKeyResponse(_message.Message):
    __slots__ = ("key",)
    KEY_FIELD_NUMBER: _ClassVar[int]
    key: str
    def __init__(self, key: _Optional[str] = ...) -> None: ...

class GetAccessRequest(_message.Message):
    __slots__ = ("key", "secret")
    KEY_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    key: str
    secret: str
    def __init__(self, key: _Optional[str] = ..., secret: _Optional[str] = ...) -> None: ...

class GetAccessResponse(_message.Message):
    __slots__ = ("permit",)
    PERMIT_FIELD_NUMBER: _ClassVar[int]
    permit: bool
    def __init__(self, permit: bool = ...) -> None: ...
