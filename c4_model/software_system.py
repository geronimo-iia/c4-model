"""SoftwareSystem model."""
from dataclasses import dataclass
from typing import Dict, Optional

from .definition import ExtendedModel, Reference

__all__ = ["SoftwareSystem", "SoftwareSystemReference"]


@dataclass(eq=False)
class SoftwareSystem(ExtendedModel):
    """Software System Notation.

    A software system is the highest level of abstraction and describes something that delivers value to its users,
    whether they are human or not.
    This includes the software system you are modelling, and the other software systems upon which your software system
    depends (or vice versa).

    Attributes:
        name (str): model name.
        extended_attributes (Dict[str, str]): an optional dict of (string, string).
        description (Optional[str]): optional description.

    """

    description: Optional[str] = None

    @classmethod
    def from_resource(cls, data: Dict) -> "SoftwareSystem":
        """Instanciate a SoftwareSystem.

        Args:
            data (Dict): dictionnary of this instance.

        Returns:
            (SoftwareSystem): a SoftwareSystem instance.
        """
        return SoftwareSystem(
            name=data["name"],
            description=data.get("description"),
            extended_attributes=data.get("extended_attributes", {}),
        )


class SoftwareSystemReference(Reference):
    """SoftwareSystem reference."""

    def __init__(self, name: str):
        super().__init__(c4_class_name=SoftwareSystem.__name__, name=name)
