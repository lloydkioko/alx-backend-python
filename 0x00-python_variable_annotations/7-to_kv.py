#!/usr/bin/env python3
"""
Type annotated to_kv function module
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple containing a string and a squared number"""
    return (k, float(v ** 2))
