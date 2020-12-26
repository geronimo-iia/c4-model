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
                m = manager.add(c(name=f"i{base}_{index}"))
                if base > 2:
                    m.attach(name=f"i{base-1}_{index%5}")

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

    def test_lookup_children(self):
        manager = C4Manager()
        self.feed(manager)
        self.assertEqual(0, len(list(manager.lookup_children(parent=Person(name="i1_0")))))
        self.assertEqual(3, len(list(manager.lookup_children(parent=SoftwareSystem(name="i2_0")))))
        self.assertEqual(3, len(list(manager.lookup_children(parent=SoftwareSystem(name="i2_1")))))
        self.assertEqual(4, len(list(manager.lookup_children(parent=Container(name="i3_0")))))
        self.assertEqual(4, len(list(manager.lookup_children(parent=Container(name="i3_1")))))
        self.assertEqual(5, len(list(manager.lookup_children(parent=Component(name="i4_0")))))
        self.assertEqual(5, len(list(manager.lookup_children(parent=Component(name="i4_1")))))
        self.assertEqual(0, len(list(manager.lookup_children(parent=CodeElement(name="i5_0")))))
