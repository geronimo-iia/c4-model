from c4_model import Person

p = Person(name="p1", description="big boss", extended_attributes={"qualifier": "vip"})
p_as_dict = p.data
print(p_as_dict)

p2 = Person.from_resource(data=p_as_dict)

assert p == p2