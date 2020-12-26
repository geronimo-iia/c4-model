"""c4 model definition."""
from pkg_resources import DistributionNotFound, get_distribution

from .code_element import CodeElement, CodeElementReference
from .component import Component, ComponentReference
from .container import Container, ContainerReference
from .definition import NAMESPACE_C4, PROVIDER_CODE, BaseModel, ExtendedModel
from .manager import C4Manager
from .person import Person, PersonReference
from .relation_ship import ModelReference, RelationShip
from .software_system import SoftwareSystem, SoftwareSystemReference

__all__ = [
    "__version__",
    "PROVIDER_CODE",
    "NAMESPACE_C4",
    "BaseModel",
    "ExtendedModel",
    "Person",
    "PersonReference",
    "SoftwareSystem",
    "SoftwareSystemReference",
    "Container",
    "ContainerReference",
    "Component",
    "ComponentReference",
    "CodeElement",
    "CodeElementReference",
    "RelationShip",
    "ModelReference",
    "C4Manager",
]

try:
    __version__ = get_distribution('c4_model').version
except DistributionNotFound:  # pragma: no cover
    __version__ = '(local)'
