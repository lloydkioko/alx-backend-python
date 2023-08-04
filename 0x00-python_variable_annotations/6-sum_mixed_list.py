#!/usr/bin/env python3
"""
Type annotated sum_mixed_list function module
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns sum of numbers in list arg"""
    return sum(mxd_list)
