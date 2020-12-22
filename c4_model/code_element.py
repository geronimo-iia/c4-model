from dataclasses import dataclass
from typing import Dict, Optional

from .component import ComponentReference
from .definition import ExtendedModel, Reference

__all__ = ["CodeElement", "CodeElementReference"]


@dataclass(eq=False)
class CodeElement(ExtendedModel):
    """CodeElement Notation.

    Code elements (e.g. classes, interfaces, etc) that are used to implement the component in scope.
    """

    parent: Optional[ComponentReference] = None
    description: Optional[str] = None

    def attach(self, name: str):
        """Attach this code element to a component."""
        self.parent = ComponentReference(name)

    @classmethod
    def from_resource(cls, data: Dict) -> "CodeElement":
        """Instanciate a CodeElement.

        Args:
            data (Dict): dictionnary of this instance.

        Returns:
            (CodeElement): a CodeElement instance.
        """
        item = CodeElement(
            name=data["name"],
            description=data.get("description"),
            extended_attributes=data.get("extended_attributes", {}),
        )
        if "parent" in data:
            item.attach(name=data["parent"]["name"])
        return item


class CodeElementReference(Reference):
    """Code element reference."""

    def __init__(self, name: str):
        super().__init__(c4_class_name=CodeElement.__name__, name=name)
