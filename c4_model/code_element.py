from dataclasses import dataclass
from typing import Dict, Optional

from .component import ComponentReference
from .definition import ExtendedModel, Reference

__all__ = ["CodeElement", "CodeElementReference"]


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
            extended_attributes=data.get("extended_attributes", {}),
        )
        if "parent" in data:
            item.attach(name=data["parent"]["name"])
        return item


class CodeElementReference(Reference):
    def __init__(self, name: str):
        super().__init__(c4_class_name=CodeElement.__name__, name=name)
