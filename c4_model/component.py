from dataclasses import dataclass
from typing import Dict, Optional

from container import ContainerReference

from .definition import ExtendedModel, Reference

__all__ = ["Component", "ComponentReference"]


@dataclass(eq=False)
class Component(ExtendedModel):
    """Component Notation.

    The word "component" is a hugely overloaded term in the software development industry,
    but in this context a component is simply a grouping of related functionality encapsulated
    behind a well-defined interface.
    If you're using a language like Java or C#, the simplest way to think of a component is that it's a collection
    of implementation classes behind an interface.
    Aspects such as how those components are packaged (e.g. one component vs many components per JAR file,
    DLL, shared library, etc) is a separate and orthogonal concern.

    An important point to note here is that all components inside a container typically execute
    in the same process space.
    """

    parent: Optional[ContainerReference] = None
    description: Optional[str] = None

    def attach(self, name: str):
        """Attach this component to a container."""
        self.parent = ContainerReference(name)

    @classmethod
    def from_resource(cls, data: Dict) -> "Component":
        item = Component(
            name=data["name"],
            description=data.get("description"),
            extended_attributes=data.get("extended_attributes", {}),
        )
        if "parent" in data:
            item.attach(name=data["parent"]["name"])
        return item


class ComponentReference(Reference):
    def __init__(self, name: str):
        super().__init__(c4_class_name=Component.__name__, name=name)
