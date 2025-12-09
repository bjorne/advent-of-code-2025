from typing import TypeVar, Generic, Iterable

T = TypeVar('T')

def minmax(it: Iterable[T]) -> tuple[T, T]:
    min = max = None
    for val in it:
        if min is None or val < min:
            min = val
        if max is None or val > max:
            max = val
    return min, max
