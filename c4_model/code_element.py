from typing import Dict, Optional
from dataclasses import asdict, dataclass, field, InitVar
from uuid import UUID, uuid3
from enum import Enum, unique
from collections import UserDict


from .definition import BaseModel, ExtendedModel, Reference, get_arn, get_resource_id
from .util import camel_to_snake

import re

from .component import ComponentReference

__all__ = [
    "Reference",
    "BaseModel",
    "Person",
    "PersonReference",
    "SoftwareSystem",
    "SoftwareSystemReference",
    "Container",
    "ContainerReference",
    "Component",
    "ComponentReference",
    "CodeElement",
    "CodeElementReference",
    "RelationShip",
    "ModelReference",
]


@dataclass(eq=False)
class CodeElement(ExtendedModel):
    parent: Optional[ComponentReference] = None
    description: Optional[str] = None

    def attach(self, name: str):
        """Attach this code element to a component."""
        self.parent = ComponentReference(name)

    @classmethod
    def from_resource(cls, data: Dict) -> "CodeElement":
        item = CodeElement(
            name=data["name"],
            description=data.get("description"),
            extended_attributes=data.get("extended_attributes"),
        )
        if "parent" in data:
            item.attach(name=data["parent"]["name"])
        return item


class CodeElementReference(Reference):
    def __init__(self, name: str):
        super().__init__(c4_class_name=CodeElement.__name__, name=name)

