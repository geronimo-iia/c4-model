import re
from collections import UserDict
from typing import Iterable

from .definition import BaseModel

__all__ = ["C4Manager"]


class C4Manager(UserDict):
    """C4Manager is an in memory dict of C4 Model."""

    def __init__(self, data: Iterable[BaseModel] = None):
        super(C4Manager, self).__init__()
        if data:
            for item in data:
                self.add(item)

    def add(self, item: BaseModel):
        """Add a model."""
        self.data[item.arn] = item

    def lookup(self, arn_query):
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
