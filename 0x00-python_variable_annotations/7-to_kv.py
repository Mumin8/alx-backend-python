#!/usr/bin/env python3
'''this will floor a float'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
  """Creates a tuple with a string key and the square of a numeric value.

  Args:
      k: A string key.
      v: An integer or float value.

  Returns:
      A tuple containing the key (string) and the square of the value (float).
  """
  return k, float(v ** 2)
