# c4 model (Work In Progress)


[![Unix Build Status](https://img.shields.io/travis/geronimo-iia/c4-model/master.svg?label=unix)](https://travis-ci.com/geronimo-iia/c4-model)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/fe669a02b4aa46b5b1faf619ba2bf382)](https://www.codacy.com/app/geronimo-iia/c4-model?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=geronimo-iia/c4-model&amp;utm_campaign=Badge_Grade)
[![PyPI Version](https://img.shields.io/pypi/v/c4-model.svg)](https://pypi.org/project/c4-model)
[![PyPI License](https://img.shields.io/pypi/l/c4-model.svg)](https://pypi.org/project/c4-model)

Versions following [Semantic Versioning](https://semver.org/)

## Overview

This module provide a simple C4 Metamodel implementation.

See [c4model](https://c4model.com/#Notation).

This project expose c4 resource:
- `Person`
- `SoftwareSystem`
- `Container`
- `Component`
- `CodeElement`
- `RelationShip`

Each of them have:
- an unique `arn` based on their type and name
- an extended attributes (dict)
- a `data` property to represent them as a dict, json etc...
- a `from_resource` method to instanciate a resource from a dict


Another class `C4Manager`, act as a container of c4 resource, with `lookup` facilities on resource's arn.


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
