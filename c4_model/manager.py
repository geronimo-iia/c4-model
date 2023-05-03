import re
from collections import UserDict
from typing import Iterable, Optional

from .definition import BaseModel
from .relation_ship import RelationShip

__all__ = ["C4Manager"]


class C4Manager(UserDict):
    """C4Manager is an in memory dict of C4 Model."""

    def __init__(self, data: Optional[Iterable[BaseModel]] = None):
        super(C4Manager, self).__init__()
        if data:
            for item in data:
                self.add(item)

    def add(self, item: BaseModel) -> BaseModel:
        """Add a model."""
        self.data[item.arn] = item
        return item

    def lookup(self, arn_query: str) -> Iterable[str]:
        """Lookup arn key for specified query.

        Args:
            arn_query (str): an arn model to lookup for
        Yields:
            (str): arn model
        """
        regex = re.compile(arn_query)
        for key in self.data.keys():
            if regex.search(key):
                yield key

    def lookup_children(self, parent: BaseModel) -> Iterable[BaseModel]:
        """Lookup children for specified parent.

        Args:
            parent_arn (BaseModel): parent

        Returns:
            (Iterable[BaseModel]): child's with specified parent arn
        """
        return filter(
            lambda item: hasattr(item, "parent") and parent == item.parent,  # type: ignore[attr-defined]
            self.data.values(),
        )

    def lookup_person(self):
        """Lookup for all person instance."""
        return self.lookup(arn_query="arn:c4:person:*")

    def lookup_software_system(self):
        """Lookup for all software system instance."""
        return self.lookup(arn_query="arn:c4:software_system:*")

    def lookup_container(self):
        """Lookup for all container instance."""
        return self.lookup(arn_query="arn:c4:container:*")

    def lookup_component(self):
        """Lookup for all component instance."""
        return self.lookup(arn_query="arn:c4:component:*")

    def lookup_code_element(self):
        """Lookup for all code element instance."""
        return self.lookup(arn_query="arn:c4:code_element:*")

    def lookup_relation_ship(self):
        """Lookup for all relation ship instance."""
        return self.lookup(arn_query="arn:c4:relation_ship:*")

    def lookup_relation_ship_with_origin(self, origin: BaseModel) -> RelationShip:
        """Lookup for all relation ship instance with specified origin."""
        return filter(
            lambda r: r.origin == origin,
            (self[arn] for arn in self.lookup_relation_ship()),  # type: ignore[return-value]
        )

    def lookup_relation_ship_with_target(self, target: BaseModel) -> RelationShip:
        """Lookup for all relation ship instance with specified target."""
        return filter(
            lambda r: r.target == target,
            (self[arn] for arn in self.lookup_relation_ship()),  # type: ignore[return-value]
        )
