"""Definition."""
from dataclasses import InitVar, asdict, dataclass, field
from typing import Dict, Optional
from uuid import UUID, uuid3

from .util import camel_to_snake

__all__ = ["PROVIDER_CODE", "NAMESPACE_C4", "get_resource_id", "get_arn", "Reference", "BaseModel", "ExtendedModel"]


PROVIDER_CODE = "c4"

NAMESPACE_C4 = UUID("51d76b7f-57a7-4a63-9d88-3c2c0490e518")


def get_resource_id(class_name: str, name: str) -> UUID:
    """Returns a resource identifier.

    Arguments:
        class_name (str): class name of model
        name (str): name of the model

    Returns:
        (UUID): a resource identifier.
    """
    return uuid3(NAMESPACE_C4, f"{class_name}:{name.replace(' ', '_').lower()}")


def get_arn(resource_type: str, resource_id) -> str:
    """Returns an arn.

    Arguments:
        resource_type (str): resource type
        resource_id (str): resource identifier

    Returns:
        (str): arn.
    """
    return f"arn:{PROVIDER_CODE}:{resource_type}:{resource_id}"


@dataclass
class Reference:
    """Internale Reference implementation."""

    name: str
    resource_type: Optional[str] = None
    resource_id: Optional[str] = None
    c4_class_name: InitVar[str] = None

    def __post_init__(self, c4_class_name: str):
        """Post build class.

        If c4_class_name is present, compute resource_type and resource_id memeber.

        Arguments:
            c4_class_name (str): optional c4_class_name
        """
        if c4_class_name:
            self.resource_type = camel_to_snake(c4_class_name)
            self.resource_id = get_resource_id(class_name=c4_class_name, name=self.name)

    @property
    def arn(self) -> str:
        """Returns arn.

        Returns:
            (str): arn of this instance
        """
        return get_arn(resource_type=self.resource_type, resource_id=self.resource_id)

    @property
    def data(self) -> Dict:
        """Returns a dictionnary of this instance.

        Returns:
            (Dict): dictionnary of this instance.
        """
        return asdict(self)

    def __eq__(self, other) -> bool:
        """Compare two instance of Reference.

        Arguments:
            other: other instance to compare.

        Returns:
            (bool): true if resource_id are equals, false either.
        """
        if other:
            return self.resource_id == other.resource_id if hasattr(other, "resource_id") else False
        return False


@dataclass
class BaseModel:
    """Abstract root model."""

    name: str

    @property
    def provider(self):
        """Returns provider.

        Returns:
            (str): provider of this instance
        """
        return PROVIDER_CODE

    @property
    def resource_type(self):
        """Returns resource type.

        Returns:
            (str): resource type of this instance
        """
        return camel_to_snake(self.__class__.__name__)

    @property
    def resource_id(self):
        """Returns resource identifier.

        Returns:
            (str): resource identifierof this instance
        """
        return get_resource_id(class_name=self.__class__.__name__, name=self.name)

    @property
    def data(self) -> Dict:
        """Returns a dictionnary of this instance.

        Returns:
            (Dict): dictionnary of this instance.
        """
        d = asdict(self)
        for (k, v) in d.items():
            if isinstance(v, Reference):
                d[k] = v.data
        return d

    @property
    def arn(self) -> str:
        """Returns arn.

        Returns:
            (str): arn of this instance
        """
        return get_arn(resource_type=self.resource_type, resource_id=self.resource_id)

    def __hash__(self) -> str:
        """Compute hash.

        Arguments:

        Returns:
           (str): a hash representation.
        """
        return self.resource_id

    def __eq__(self, other):
        """Compare two instance of BaseModel.

        Arguments:
            other: other instance to compare.

        Returns:
            (bool): true if resource_id are equals, false either.
        """
        if other:
            return self.resource_id == other.resource_id if hasattr(other, "resource_id") else False
        return False

    @classmethod
    def from_resource(cls, data: Dict) -> "BaseModel":
        """Instanciate a member of c4 model.

        Arguments:
            data (Dict): dictionnary of this instance.

        Raises:
            RuntimeError: base class always raise error.
        """
        raise RuntimeError("Should not be called")


@dataclass(eq=False)
class ExtendedModel(BaseModel):
    """Add extended attributes."""

    extended_attributes: Dict[str, str] = field(default_factory=dict)
