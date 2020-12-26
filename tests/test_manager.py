import unittest

from c4_model import *


class TestC4Magnager(unittest.TestCase):
    def test_add_items(self):
        manager = C4Manager()
        self.assertEqual(0, len(manager))
        p = Person(name="p1")
        manager.add(p)
        self.assertEqual(1, len(manager))
        self.assertTrue(p.arn in manager)
        self.assertEqual(p, manager.get(p.arn))

    def feed(self, manager):
        base = 0
        for c in [Person, SoftwareSystem, Container, Component, CodeElement]:
            base += 1
            for index in range(base * 5):
                manager.add(c(name=f"i{base}_{index}"))

    def test_dump(self):
        manager = C4Manager()
        self.feed(manager)
        self.assertEqual(75, len(manager))
        m = C4Manager(data=manager.values())
        self.assertEqual(75, len(m))

    def test_lookup(self):
        manager = C4Manager()
        self.feed(manager)
        self.assertEqual(5, len(list(manager.lookup_person())))
        self.assertEqual(10, len(list(manager.lookup_software_system())))
        self.assertEqual(15, len(list(manager.lookup_container())))
        self.assertEqual(20, len(list(manager.lookup_component())))
        self.assertEqual(25, len(list(manager.lookup_code_element())))
        self.assertEqual(0, len(list(manager.lookup_relation_ship())))

    def test_empty_lookup(self):
        manager = C4Manager()
        self.assertEqual(0, len(list(manager.lookup_person())))