
#!/usr/bin/env python3
""" Complex types - functions """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        type-annotated function make_multiplier
            takes a float multiplier as argument
                returns a function that multiplies a float by multiplier.
                    """
    return lambda x: x * multiplier
