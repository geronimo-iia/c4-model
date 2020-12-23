"""Definition."""
from dataclasses import InitVar, asdict, dataclass, field
from typing import Dict, Optional
from uuid import UUID, uuid3

from .util import camel_to_snake

__all__ = ["PROVIDER_CODE", "NAMESPACE_C4", "get_resource_id", "get_arn", "Reference", "BaseModel", "ExtendedModel"]


PROVIDER_CODE = "c4"

NAMESPACE_C4 = UUID("51d76b7f-57a7-4a63-9d88-3c2c0490e518")


def get_resource_id(class_name: str, name: str) -> str:
    """Return a resource identifier.

    Args:
        class_name (str): class name of model
        name (str): name of the model

    Returns:
        (str): a resource identifier.
    """
    return str(uuid3(NAMESPACE_C4, f"{class_name}:{name.replace(' ', '_').lower()}"))


def get_arn(resource_type: str, resource_id: str) -> str:
    """Return an arn.

    Args:
        resource_type (str): resource type
        resource_id (str): resource identifier

    Returns:
        (str): arn.
    """
    return f"arn:{PROVIDER_CODE}:{resource_type}:{resource_id}"


@dataclass
class Reference:
    """Internale Reference implementation.

    Attributes:
        name (str): resource name
        resource_type (str): resource type
        resource_id (str): resource identifier
    """

    name: str
    resource_type: Optional[str] = None
    resource_id: Optional[str] = None
    c4_class_name: InitVar[str] = None

    def __post_init__(self, c4_class_name: str):
        """Post build class.

        If c4_class_name is present, compute resource_type and resource_id memeber.

        Args:
            c4_class_name (str): optional c4_class_name

        Raises:
            (RuntimeError): if resource_type or resource_id is none.
        """
        if c4_class_name:
            self.resource_type = camel_to_snake(c4_class_name)
            self.resource_id = get_resource_id(class_name=c4_class_name, name=self.name)
        if not self.resource_type or not self.resource_id:
            raise RuntimeError("Missing c4_class_name")

    @property
    def arn(self) -> str:
        """Return arn.

        Returns:
            (str): arn of this instance
        """
        return get_arn(resource_type=self.resource_type, resource_id=self.resource_id)  # type: ignore[arg-type]

    @property
    def data(self) -> Dict:
        """Return a dictionnary of this instance.

        Returns:
            (Dict): dictionnary of this instance.
        """
        return asdict(self)

    def __eq__(self, other) -> bool:
        """Compare two instance of Reference.

        Args:
            other: other instance to compare.

        Returns:
            (bool): true if resource_id are equals, false either.
        """
        if other:
            return self.resource_id == other.resource_id if hasattr(other, "resource_id") else False
        return False

    def __hash__(self) -> int:
        """Compute hash.

        Returns:
           (int): a hash representation.
        """
        return hash(self.resource_id)


@dataclass
class BaseModel:
    """Abstract c4 root model.

    Attributes:
        name (str): model name.
    """

    name: str

    @property
    def provider(self):
        """Return provider.

        Returns:
            (str): provider of this instance
        """
        return PROVIDER_CODE

    @property
    def resource_type(self):
        """Return resource type.

        Returns:
            (str): resource type of this instance
        """
        return camel_to_snake(self.__class__.__name__)

    @property
    def resource_id(self):
        """Return resource identifier.

        Returns:
            (str): resource identifierof this instance
        """
        return get_resource_id(class_name=self.__class__.__name__, name=self.name)

    @property
    def data(self) -> Dict:
        """Return a dictionnary of this instance.

        Returns:
            (Dict): dictionnary of this instance.
        """
        return asdict(self)

    @property
    def arn(self) -> str:
        """Return arn.

        Returns:
            (str): arn of this instance
        """
        return get_arn(resource_type=self.resource_type, resource_id=self.resource_id)

    def __hash__(self) -> int:
        """Compute hash.

        Returns:
           (int): a hash representation.
        """
        return hash(self.resource_id)

    def __eq__(self, other):
        """Compare two instance of BaseModel.

        Args:
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

        Args:
            data (Dict): dictionnary of this instance.

        Raises:
            RuntimeError: base class always raise error.
        """
        raise RuntimeError("Should not be called")


@dataclass(eq=False)
class ExtendedModel(BaseModel):
    """Add extended attributes.

    Attributes:
        extended_attributes (Dict[str, str]): an optional dict of (string, string)
    """

    extended_attributes: Dict[str, str] = field(default_factory=dict)
