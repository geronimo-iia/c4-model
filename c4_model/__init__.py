"""c4 model definition."""
from pkg_resources import get_distribution, DistributionNotFound
from .definition import PROVIDER_CODE, NAMESPACE_C4, BaseModel

from .person import Person
from .software_system import SoftwareSystem
from .container import Container
from .component import Component
from .code_element import CodeElement
from .relation_ship import RelationShip


__all__ = [
    "__version__",
    "PROVIDER_CODE",
    "NAMESPACE_C4",
    "BaseModel",
    "Person",
    "SoftwareSystem",
    "Container",
    "Component",
    "CodeElement",
    "RelationShip",
]

try:
    __version__ = get_distribution('c4_model').version
except DistributionNotFound:  # pragma: no cover
    __version__ = '(local)'
