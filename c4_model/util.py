import re

__all__ = ["camel_to_snake"]

# __camel_to_snake optimisation pattern
_pattern_1 = re.compile("(.)([A-Z][a-z]+)")
_pattern_2 = re.compile("([a-z0-9])([A-Z])")


def camel_to_snake(name: str) -> str:
    """Convert camel case string to snake case.

    Arguments:
        name (str): a name

    Returns:
        (str): a camelized string
    """
    name = _pattern_1.sub(r"\1_\2", name)
    return _pattern_2.sub(r"\1_\2", name).lower()
