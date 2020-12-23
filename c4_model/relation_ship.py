from dataclasses import dataclass, field
from enum import Enum, unique
from typing import Dict, Optional

from .code_element import CodeElement, CodeElementReference
from .component import Component, ComponentReference
from .container import Container, ContainerReference
from .definition import BaseModel, Reference
from .person import Person, PersonReference
from .software_system import SoftwareSystem, SoftwareSystemReference
from .util import camel_to_snake

__all__ = ["RelationShip", "ModelReference"]


@dataclass(eq=False)
class RelationShip(BaseModel):
    """RelationShip Notation.

    Attributes:
        name (str): model name.
        origin (Reference): origin of this relationship
        target (Reference): target of this relationship
        description (Optional[str]): optional description
        technology (Optional[str]): optional technology
        extended_attributes (Dict[str, str]): optional extra attributes
    """

    origin: Reference
    target: Reference
    description: Optional[str] = None
    technology: Optional[str] = None
    extended_attributes: Dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_resource(cls, data: Dict) -> "RelationShip":
        """Instanciate a RelationShip.

        Args:
            data (Dict): dictionnary of this instance.

        Returns:
            (RelationShip): a RelationShip instance.
        """
        item = RelationShip(
            name=data["name"],
            origin=ModelReference.from_resource_type(resource_type=data["origin"]["resource_type"]).create_reference(
                name=data["origin"]["name"]
            ),
            target=ModelReference.from_resource_type(resource_type=data["target"]["resource_type"]).create_reference(
                name=data["target"]["name"]
            ),
            description=data.get("description"),
            technology=data.get("technology"),
            extended_attributes=data.get("extended_attributes", {}),
        )
        return item


@unique
class ModelReference(Enum):
    """Enumerate referencable model."""

    PERSON = (PersonReference, camel_to_snake(Person.__name__))
    SOFTWARE_SYSTEM = (SoftwareSystemReference, camel_to_snake(SoftwareSystem.__name__))
    CONTAINER = (ContainerReference, camel_to_snake(Container.__name__))
    COMPONENT = (ComponentReference, camel_to_snake(Component.__name__))
    CODE_ELEMENT = (CodeElementReference, camel_to_snake(CodeElement.__name__))

    def create_reference(self, name: str):
        """Create a reference instance for the specified name."""
        return self.value[0](name=name)

    @classmethod
    def from_name(cls, name: str) -> "ModelReference":
        """Find ModelReference instance for specified name.

        Args:
            name (str): c4 model name

        Returns:
            (ModelReference): the instance

        Raises:
            (RuntimeError): if no member is associated with the specified name.
        """
        _upper_name = name.upper()
        for model in ModelReference:
            if model.name == _upper_name:
                return model
        raise RuntimeError(f"{name} not found in ModelReference")

    @classmethod
    def from_resource_type(cls, resource_type: str) -> "ModelReference":
        """Find ModelReference instance for specified resource type.

        Args:
            resource_type (str): c4 resource type name

        Returns:
            (ModelReference): the instance

        Raises:
            (RuntimeError): if no member is associated with the specified resource type.
        """
        for model in ModelReference:
            if model.value[1] == resource_type:
                return model
        raise RuntimeError(f"{resource_type} not found in ModelReference")
