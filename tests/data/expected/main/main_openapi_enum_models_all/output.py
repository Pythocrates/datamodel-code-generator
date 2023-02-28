# generated by datamodel-codegen:
#   filename:  enum_models.yaml
#   timestamp: 2019-07-26T00:00:00+00:00

from __future__ import annotations

from typing import List, Literal, Optional, Union

from pydantic import BaseModel, Field


class Pet(BaseModel):
    id: int
    name: str
    tag: Optional[str] = None
    kind: Optional[Literal['dog', 'cat']] = None
    type: Optional[Literal['animal']] = None
    number: Literal[1]
    boolean: Literal[True]


class Pets(BaseModel):
    __root__: List[Pet]


class Animal(BaseModel):
    kind: Optional[Literal['snake', 'rabbit']] = None


class Error(BaseModel):
    code: int
    message: str


class EnumObject(BaseModel):
    type: Optional[Literal['a', 'b']] = None


class EnumRoot(BaseModel):
    __root__: Literal['a', 'b']


class IntEnum(BaseModel):
    __root__: Literal[1, 2]


class AliasEnum(BaseModel):
    __root__: Literal[1, 2, 3]


class MultipleTypeEnum(BaseModel):
    __root__: Literal['red', 'amber', 'green', 42]


class SingleEnum(BaseModel):
    __root__: Literal['pet']


class ArrayEnum(BaseModel):
    __root__: List[Union[Literal['cat'], Literal['dog']]]


class NestedNullableEnum(BaseModel):
    nested_version: Optional[
        Literal['RC1', 'RC1N', 'RC2', 'RC2N', 'RC3', 'RC4']
    ] = Field('RC1', description='nullable enum', example='RC2')


class Version(BaseModel):
    __root__: Optional[Literal['RC1', 'RC1N', 'RC2', 'RC2N', 'RC3', 'RC4']] = Field(
        'RC1', description='nullable enum', example='RC2'
    )
