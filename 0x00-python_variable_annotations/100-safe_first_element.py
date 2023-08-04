#!/usr/bin/env python3
"""
Type annotated safe_first_element function module
"""
from typing import Any, Optional, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """safe_first_element function"""
    if lst:
        return lst[0]
    else:
        return None
