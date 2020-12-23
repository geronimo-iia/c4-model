import unittest

from c4_model import *
from c4_model.code_element import CodeElementReference
from c4_model.component import ComponentReference
from c4_model.container import ContainerReference
from c4_model.person import PersonReference
from c4_model.relation_ship import ModelReference
from c4_model.software_system import SoftwareSystemReference


class TestC4(unittest.TestCase):
    def test_person(self):
        p = Person(name="p1")
        self.assertEqual("p1", p.name)
        self.assertIsNone(p.description)
        self.assertEqual("c4", p.provider)
        self.assertEqual("7fd91543-6b1f-3a69-91b9-9ae50369fab3", p.resource_id)
        self.assertEqual("person", p.resource_type)
        self.assertEqual("arn:c4:person:7fd91543-6b1f-3a69-91b9-9ae50369fab3", p.arn)
        p.description = "test"
        self.assertEqual("test", p.description)
        self.assertEqual({"description": "test", "name": "p1", "extended_attributes": {}}, p.data)

        # compare on name
        self.assertEqual(p, Person(name="p1", description="test"))
        self.assertEqual(p, Person(name="p1", description="another description"))
        self.assertNotEqual(p, Person(name="p2"))
        # ref is equals
        self.assertEqual(p, PersonReference(name="p1"))

    def test_person_reference(self):
        ref = PersonReference(name="p1")
        self.assertEqual("p1", ref.name)
        self.assertEqual("arn:c4:person:7fd91543-6b1f-3a69-91b9-9ae50369fab3", ref.arn)
        self.assertEqual(
            {"name": "p1", "resource_id": "7fd91543-6b1f-3a69-91b9-9ae50369fab3", "resource_type": "person"},
            ref.data,
        )

        self.assertEqual(ref, PersonReference(name="p1"))
        self.assertNotEqual(ref, PersonReference(name="p2"))

    def test_person_from_resource(self):
        a = Person(name="p1", description="test")
        b = Person.from_resource(data=a.data)
        self.assertIsNotNone(b)
        self.assertEqual(a, b)
        self.assertEqual("p1", b.name)
        self.assertEqual("test", b.description)

    def test_software_system(self):
        p = SoftwareSystem(name="s1", description="amazing")
        self.assertEqual("s1", p.name)
        self.assertEqual("amazing", p.description)
        self.assertEqual("c4", p.provider)
        self.assertEqual("def66b36-2de7-31ce-bab6-91401ff441b1", p.resource_id)
        self.assertEqual("software_system", p.resource_type)
        self.assertEqual("arn:c4:software_system:def66b36-2de7-31ce-bab6-91401ff441b1", p.arn)

        self.assertEqual({"description": "amazing", "name": "s1", "extended_attributes": {}}, p.data)

        # compare on name
        self.assertEqual(p, SoftwareSystem(name="s1", description="test"))
        self.assertEqual(p, SoftwareSystem(name="s1", description="another description"))
        self.assertNotEqual(p, SoftwareSystem(name="p2"))

        self.assertNotEqual(p, Person(name="s1"))

        # ref is equals
        self.assertEqual(p, SoftwareSystemReference(name="s1"))

    def test_software_system_reference(self):
        ref = SoftwareSystemReference(name="p1")
        self.assertEqual("p1", ref.name)
        self.assertEqual("arn:c4:software_system:09cdf16f-a6d8-3d00-9627-ffc972c55444", ref.arn)
        self.assertEqual(
            {
                "name": "p1",
                "resource_id": "09cdf16f-a6d8-3d00-9627-ffc972c55444",
                "resource_type": "software_system",
            },
            ref.data,
        )

        self.assertEqual(ref, SoftwareSystemReference(name="p1"))
        self.assertNotEqual(ref, SoftwareSystemReference(name="p2"))
        self.assertNotEqual(ref, PersonReference(name="p1"))

    def test_software_system_from_resource(self):
        a = SoftwareSystem(name="p1", description="test")
        b = SoftwareSystem.from_resource(data=a.data)
        self.assertIsNotNone(b)
        self.assertEqual(a, b)
        self.assertEqual("p1", b.name)
        self.assertEqual("test", b.description)


    def test_container(self):
        p = Container(name="s1", description="amazing container", technology="docker")
        self.assertEqual("s1", p.name)
        self.assertEqual("amazing container", p.description)
        self.assertEqual("docker", p.technology)
        self.assertEqual("c4", p.provider)
        self.assertEqual("7eed994b-1cc3-3d80-a9c1-5721146f76cb", p.resource_id)
        self.assertEqual("container", p.resource_type)
        self.assertEqual("arn:c4:container:7eed994b-1cc3-3d80-a9c1-5721146f76cb", p.arn)

        self.assertEqual(
            {
                "description": "amazing container",
                "parent": None,
                "technology": "docker",
                "name": "s1",
                "extended_attributes": {},
            },
            p.data,
        )

        # compare on name
        self.assertEqual(p, Container(name="s1", description="test"))
        self.assertEqual(p, Container(name="s1", description="another description"))
        self.assertNotEqual(p, Container(name="p2"))

        self.assertNotEqual(p, Person(name="s1"))

        # ref is equals
        self.assertEqual(p, ContainerReference(name="s1"))

    def test_container_reference(self):
        ref = ContainerReference(name="p1")
        self.assertEqual("p1", ref.name)
        self.assertEqual("arn:c4:container:0266db1f-3b7c-3796-a899-00b34cab6f93", ref.arn)
        self.assertEqual(
            {"name": "p1", "resource_id": "0266db1f-3b7c-3796-a899-00b34cab6f93", "resource_type": "container"},
            ref.data,
        )

        self.assertEqual(ref, ContainerReference(name="p1"))
        self.assertNotEqual(ref, ContainerReference(name="p2"))
        self.assertNotEqual(ref, PersonReference(name="p1"))

    def test_container_attach(self):
        p = Container(name="s1", description="amazing container", technology="docker")
        self.assertIsNone(p.parent)
        p.attach("soft1")
        self.assertIsNotNone(p.parent)
        self.assertEqual(p.parent, SoftwareSystemReference(name="soft1"))
        self.assertEqual(p.parent, SoftwareSystem(name="soft1"))

    def test_container_from_resource(self):
        a = Container(name="p1", description="test", technology="docker")
        b = Container.from_resource(data=a.data)
        self.assertIsNotNone(b)
        self.assertEqual(a, b)
        self.assertEqual("p1", b.name)
        self.assertEqual("test", b.description)
        self.assertEqual("docker", b.technology)

        a.attach("soft1")
        b = Container.from_resource(data=a.data)
        self.assertEqual(SoftwareSystem(name="soft1"), b.parent)

    def test_component(self):
        p = Component(name="s1", description="amazing component")
        self.assertEqual("s1", p.name)
        self.assertEqual("amazing component", p.description)
        self.assertIsNone(p.parent)
        self.assertEqual("c4", p.provider)
        self.assertEqual("3ebca1af-c7d1-3240-9763-4c820d2d950c", p.resource_id)
        self.assertEqual("component", p.resource_type)
        self.assertEqual("arn:c4:component:3ebca1af-c7d1-3240-9763-4c820d2d950c", p.arn)

        self.assertEqual(
            {"description": "amazing component", "parent": None, "name": "s1", "extended_attributes": {}}, p.data
        )

        # compare on name
        self.assertEqual(p, Component(name="s1", description="test"))
        self.assertEqual(p, Component(name="s1", description="another description"))
        self.assertNotEqual(p, Component(name="p2"))

        self.assertNotEqual(p, Person(name="s1"))

        # ref is equals
        self.assertEqual(p, ComponentReference(name="s1"))

    def test_component_reference(self):
        ref = ComponentReference(name="p1")
        self.assertEqual("p1", ref.name)
        self.assertEqual("arn:c4:component:776690e1-ec29-39ba-89bf-66a3faa1a630", ref.arn)
        self.assertEqual(
            {"name": "p1", "resource_id": "776690e1-ec29-39ba-89bf-66a3faa1a630", "resource_type": "component"},
            ref.data,
        )

        self.assertEqual(ref, ComponentReference(name="p1"))
        self.assertNotEqual(ref, ComponentReference(name="p2"))
        self.assertNotEqual(ref, PersonReference(name="p1"))

    def test_component_attach(self):
        p = Component(name="s1", description="amazing component")
        self.assertIsNone(p.parent)
        p.attach("soft1")
        self.assertIsNotNone(p.parent)
        self.assertEqual(p.parent, ContainerReference(name="soft1"))
        self.assertEqual(p.parent, Container(name="soft1"))
        self.assertEqual(
            {
                "description": "amazing component",
                "name": "s1",
                "extended_attributes": {},
                "parent": {
                    "name": "soft1",
                    "resource_id": "be6a2615-3c7c-3315-ac94-68c221553e78",
                    "resource_type": "container",
                },
            },
            p.data,
        )

    def test_component_from_resource(self):
        a = Component(name="p1", description="test")
        b = Component.from_resource(data=a.data)
        self.assertIsNotNone(b)
        self.assertEqual(a, b)
        self.assertEqual("p1", b.name)
        self.assertEqual("test", b.description)

        a.attach("soft1")
        b = Component.from_resource(data=a.data)
        self.assertEqual(ContainerReference(name="soft1"), b.parent)


    def test_code_element(self):
        p = CodeElement(name="s1", description="amazing code element")
        self.assertEqual("s1", p.name)
        self.assertEqual("amazing code element", p.description)
        self.assertIsNone(p.parent)
        self.assertEqual("c4", p.provider)
        self.assertEqual("c24793ba-7a0c-3597-aae3-24aa39c127e2", p.resource_id)
        self.assertEqual("code_element", p.resource_type)
        self.assertEqual("arn:c4:code_element:c24793ba-7a0c-3597-aae3-24aa39c127e2", p.arn)

        self.assertEqual(
            {"description": "amazing code element", "parent": None, "name": "s1", "extended_attributes": {}}, p.data
        )

        # compare on name
        self.assertEqual(p, CodeElement(name="s1", description="test"))
        self.assertEqual(p, CodeElement(name="s1", description="another description"))
        self.assertNotEqual(p, CodeElement(name="p2"))

        self.assertNotEqual(p, Person(name="s1"))

        # ref is equals
        self.assertEqual(p, CodeElementReference(name="s1"))

    def test_code_element_reference(self):
        ref = CodeElementReference(name="p1")
        self.assertEqual("p1", ref.name)
        self.assertEqual("arn:c4:code_element:044a817c-a0b2-3a87-bc3d-3caf272e5769", ref.arn)
        self.assertEqual(
            {
                "name": "p1",
                "resource_id": "044a817c-a0b2-3a87-bc3d-3caf272e5769",
                "resource_type": "code_element",
            },
            ref.data,
        )

        self.assertEqual(ref, CodeElementReference(name="p1"))
        self.assertNotEqual(ref, CodeElementReference(name="p2"))
        self.assertNotEqual(ref, PersonReference(name="p1"))

    def test_code_element_attach(self):
        p = CodeElement(name="s1", description="amazing component")
        self.assertIsNone(p.parent)
        p.attach("soft1")
        self.assertIsNotNone(p.parent)
        self.assertEqual(p.parent, Component(name="soft1"))
        self.assertEqual(p.parent, ComponentReference(name="soft1"))
        self.assertEqual(
            {
                "description": "amazing component",
                "name": "s1",
                "parent": {
                    "name": "soft1",
                    "resource_id": "3ca2a13b-43fa-3ecd-a872-5657f036d004",
                    "resource_type": "component",
                },
                "extended_attributes": {},
            },
            p.data,
        )


    def test_code_element_from_resource(self):
        a = CodeElement(name="p1", description="test")
        b = CodeElement.from_resource(data=a.data)
        self.assertIsNotNone(b)
        self.assertEqual(a, b)
        self.assertEqual("p1", b.name)
        self.assertEqual("test", b.description)

        a.attach("soft1")
        b = CodeElement.from_resource(data=a.data)
        self.assertEqual(ComponentReference(name="soft1"), b.parent)


    def test_relation_ship(self):
        r = RelationShip(
            name="test", origin=ContainerReference(name="container"), target=ContainerReference(name="target_container")
        )
        self.assertEqual("test", r.name)
        self.assertEqual("arn:c4:relation_ship:a619e61a-4ec6-3872-9cd7-6e42d3ff93c6", r.arn)
        self.assertIsNone(r.description)
        self.assertIsNone(r.technology)
        self.assertEqual(r.origin, Container(name="container"))
        self.assertEqual(r.target, ContainerReference(name="target_container"))
        self.assertEqual(
            {
                "description": None,
                "name": "test",
                "origin": {
                    "name": "container",
                    "resource_id": "056cf4be-829b-3756-bf5a-453419b65488",
                    "resource_type": "container",
                },
                "target": {
                    "name": "target_container",
                    "resource_id": "f2efe0b7-4c11-366c-b4bd-7071e21611e2",
                    "resource_type": "container",
                },
                "technology": None,
                "extended_attributes": {},
            },
            r.data,
        )

    def test_model_reference(self):
        self.assertEqual(ModelReference.PERSON.create_reference("aname"), PersonReference("aname"))

        self.assertEqual(ModelReference.SOFTWARE_SYSTEM.create_reference("aname"), SoftwareSystemReference("aname"))
        self.assertEqual(ModelReference.CONTAINER.create_reference("aname"), ContainerReference("aname"))
        self.assertEqual(ModelReference.COMPONENT.create_reference("aname"), ComponentReference("aname"))
        self.assertEqual(ModelReference.CODE_ELEMENT.create_reference("aname"), CodeElementReference("aname"))

    def test_model_reference_lookup_by_name(self):
        self.assertEqual(ModelReference.PERSON, ModelReference.from_name("person"))
        self.assertEqual(ModelReference.SOFTWARE_SYSTEM, ModelReference.from_name("software_system"))
        self.assertEqual(ModelReference.CONTAINER, ModelReference.from_name("container"))
        self.assertEqual(ModelReference.COMPONENT, ModelReference.from_name("component"))
        self.assertEqual(ModelReference.CODE_ELEMENT, ModelReference.from_name("code_element"))

    def test_model_reference_lookup_by_resource_type(self):
        self.assertEqual(ModelReference.PERSON, ModelReference.from_resource_type("person"))
        self.assertEqual(ModelReference.SOFTWARE_SYSTEM, ModelReference.from_resource_type("software_system"))
        self.assertEqual(ModelReference.CONTAINER, ModelReference.from_resource_type("container"))
        self.assertEqual(ModelReference.COMPONENT, ModelReference.from_resource_type("component"))
        self.assertEqual(ModelReference.CODE_ELEMENT, ModelReference.from_resource_type("code_element"))
