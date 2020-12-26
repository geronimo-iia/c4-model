from dataclasses import dataclass
from typing import Dict, Optional

from .definition import ExtendedModel, Reference
from .software_system import SoftwareSystemReference

__all__ = ["Container", "ContainerReference"]


@dataclass(eq=False)
class Container(ExtendedModel):
    """Container Notation.

    A container represents something that hosts code or data.
    A container is something that needs to be running in order for the overall software system to work.

    A container is essentially a context or boundary inside which some code is executed or some data is stored.
    And each container is a separately deployable/runnable thing or runtime environment,
    typically (but not always) running in its own process space.
    Because of this, communication between containers typically takes the form of an inter-process communication.

    Attributes:
        name (str): model name.
        extended_attributes (Dict[str, str]): an optional dict of (string, string).
        description (Optional[str]): optional description.
        technology (Optional[str]): optional technology.
        parent (Optional[SoftwareSystemReference]): optional SoftwareSystem parent.

    """

    parent: Optional[SoftwareSystemReference] = None
    technology: Optional[str] = None
    description: Optional[str] = None

    def attach(self, name: str) -> SoftwareSystemReference:
        """Attach this container to a software system.

        Args:
            name (str): name of parent

        Returns:
            (SoftwareSystemReference): parent reference
        """
        self.parent = SoftwareSystemReference(name)
        return self.parent

    @classmethod
    def from_resource(cls, data: Dict) -> "Container":
        """Instanciate a Container.

        Args:
            data (Dict): dictionnary of this instance.

        Returns:
            (Container): a Container instance.
        """
        item = Container(
            name=data["name"],
            technology=data.get("technology"),
            description=data.get("description"),
            extended_attributes=data.get("extended_attributes", {}),
        )
        if "parent" in data and data["parent"] and "name" in data["parent"]:
            item.attach(name=data["parent"]["name"])
        return item


class ContainerReference(Reference):
    """Container reference."""

    def __init__(self, name: str):
        super().__init__(c4_class_name=Container.__name__, name=name)
