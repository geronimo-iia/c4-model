"""c4 model definition."""
from pkg_resources import DistributionNotFound, get_distribution

from .code_element import CodeElement
from .component import Component
from .container import Container
from .definition import NAMESPACE_C4, PROVIDER_CODE, BaseModel, ExtendedModel
from .manager import C4Manager
from .person import Person
from .relation_ship import RelationShip
from .software_system import SoftwareSystem

__all__ = [
    "__version__",
    "PROVIDER_CODE",
    "NAMESPACE_C4",
    "BaseModel",
    "ExtendedModel",
    "Person",
    "SoftwareSystem",
    "Container",
    "Component",
    "CodeElement",
    "RelationShip",
    "C4Manager",
]

try:
    __version__ = get_distribution('c4_model').version
except DistributionNotFound:  # pragma: no cover
    __version__ = '(local)'
