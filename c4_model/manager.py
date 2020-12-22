from typing import Dict, Optional
import re
from collections import UserDict
from .definition import BaseModel

__all__ = ["C4Manager"]


class C4Manager(UserDict):
    """C4Manager is an in memory dict of C4 Model."""

    def __init__(self, dict=none):
        super("C4Manager", self).__init__(dict=dict)

    def add(self, item: BaseModel):
        self.data[item.arn] = item

    def lookup(self, arn_query):
        regex = re.compile(arn_query)
        for key in self.data.keys():
            if regex.search(key):
                yield key

    def lookup_person(self):
        return self.lookup(arn_query="arn:c4:person:*")

    def lookup_software_system(self):
        return self.lookup(arn_query="arn:c4:software_system:*")

    def lookup_container(self):
        return self.lookup(arn_query="arn:c4:container:*")

    def lookup_component(self):
        return self.lookup(arn_query="arn:c4:component:*")

    def lookup_code_element(self):
        return self.lookup(arn_query="arn:c4:code_element:*")

    def lookup_relation_ship(self):
        return self.lookup(arn_query="arn:c4:relation_ship:*")
