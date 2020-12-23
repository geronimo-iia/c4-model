from dataclasses import dataclass
from typing import Dict, Optional

from .component import ComponentReference
from .definition import ExtendedModel, Reference

__all__ = ["CodeElement", "CodeElementReference"]


@dataclass(eq=False)
class CodeElement(ExtendedModel):
    """CodeElement Notation.

    Code elements (e.g. classes, interfaces, etc) that are used to implement the component in scope.

    Attributes:
        name (str): model name.
        extended_attributes (Dict[str, str]): an optional dict of (string, string).
        description (Optional[str]): optional description.
        parent (Optional[ComponentReference]): optional Component parent.
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
            (CodeElement): a CodeElement
        """
        item = CodeElement(
            name=data["name"],
            description=data.get("description"),
            extended_attributes=data.get("extended_attributes", {}),
        )
        if "parent" in data and data["parent"] and "name" in data["parent"]:
            item.attach(name=data["parent"]["name"])
        return item


class CodeElementReference(Reference):
    """Code element reference."""

    def __init__(self, name: str):
        super().__init__(c4_class_name=CodeElement.__name__, name=name)
