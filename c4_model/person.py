"""Person Model."""
from dataclasses import dataclass
from typing import Dict, Optional

from .definition import ExtendedModel, Reference

__all__ = ["Person", "PersonReference"]


@dataclass(eq=False)
class Person(ExtendedModel):
    """Person Notation.

    However you think about your users (as actors, roles, personas, etc),
    people are the various human users of your software system.
    A person represents one of the human users of your software system (e.g. actors, roles, personas, etc).

    Attributes:
        name (str): model name.
        extended_attributes (Dict[str, str]): an optional dict of (string, string).
        description (Optional[str]): optional description.
    """

    description: Optional[str] = None

    @classmethod
    def from_resource(cls, data: Dict) -> "Person":
        """Instanciate a Person.

        Args:
            data (Dict): dictionnary of this instance.

        Returns:
            (Person): a Person instance.
        """
        return Person(
            name=data["name"],
            description=data.get("description"),
            extended_attributes=data.get("extended_attributes", {}),
        )


class PersonReference(Reference):
    """Person reference."""

    def __init__(self, name: str):
        super().__init__(c4_class_name=Person.__name__, name=name)
