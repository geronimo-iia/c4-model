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
    """

    description: Optional[str] = None

    @classmethod
    def from_resource(cls, data: Dict) -> "Person":
        return Person(
            name=data["name"],
            description=data.get("description"),
            extended_attributes=data.get("extended_attributes", {}),
        )


class PersonReference(Reference):
    def __init__(self, name: str):
        super().__init__(c4_class_name=Person.__name__, name=name)
