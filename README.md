# c4 model


[![Travis Build Status](https://img.shields.io/travis/geronimo-iia/c4-model/master.svg?label=unix)](https://travis-ci.com/geronimo-iia/c4-model)
[![Codecov](https://codecov.io/gh/geronimo-iia/c4-model/branch/master/graph/badge.svg)](https://codecov.io/gh/geronimo-iia/c4-model)
[![PyPI Version](https://img.shields.io/pypi/v/c4-model.svg)](https://pypi.org/project/c4-model)
[![PyPI License](https://img.shields.io/pypi/l/c4-model.svg)](https://pypi.org/project/c4-model)

Versions following [Semantic Versioning](https://semver.org/)

## Overview

This module provide a simple C4 Metamodel implementation.

See [c4model](https://c4model.com/#Notation).

This project expose c4 resource:
- [Person](https://geronimo-iia.github.io/c4-model/api.html#c4_model.Person)
- [SoftwareSystem](https://geronimo-iia.github.io/c4-model/api.html#c4_model.SoftwareSystem)
- [Container](https://geronimo-iia.github.io/c4-model/api.html#c4_model.Container)
- [Component](https://geronimo-iia.github.io/c4-model/api.html#c4_model.Component)
- [CodeElement](https://geronimo-iia.github.io/c4-model/api.html#c4_model.CodeElement)
- [RelationShip](https://geronimo-iia.github.io/c4-model/api.html#c4_model.RelationShip)

Each of them have:
- an unique `arn` based on their type and name
- an extended attributes (dict)
- a `data` property to represent them as a dict, json etc...
- a `from_resource` method to instanciate a resource from a dict


Another class [C4Manager](https://geronimo-iia.github.io/c4-model/api.html#c4_model.C4Manager), act as a container of c4 resource, with `lookup` facilities on resource's arn.


## Installation

Install this library directly into an activated virtual environment:

```text
$ pip install c4-model
```

or add it to your [Poetry](https://poetry.eustace.io/) project:

```text
$ poetry add c4-model
```

## Usage

After installation, the package can imported:

```text
$ python
>>> import c4_model
>>> c4_model.__version__
```

See [documentation](https://geronimo-iia.github.io/c4-model) for more detail on each resources.

To create a `Person`, you can do:

```
from c4_model import Person
p = Person(name="p1")
p.description = "big boss"
p.extended_attributes["qualifier"] = "vip"

print(p.arn)

>>> "arn:c4:person:7fd91543-6b1f-3a69-91b9-9ae50369fab3"
```

or 

```
from c4_model import Person
p = Person(name="p1", description="big boss", extended_attributes={"qualifier": "vip"})
```

To deal with dict:

```
from c4_model import Person
p = Person(name="p1", description="big boss", extended_attributes={"qualifier": "vip"})

p_as_dict = p.data
print(p_as_dict)

>>> {'name': 'p1', 'extended_attributes': {'qualifier': 'vip'}, 'description': 'big boss'}

# load a resource
p2 = Person.from_resource(data=p_as_dict)

# equality is here
assert p == p2
```



