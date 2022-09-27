"""
    query filter
"""
import re
from operator import itemgetter
from typing import Iterator, Any, List, Union, Iterable


def query_filter(data: Union[Iterator[str], Iterable[str]], value: str) -> Iterator[str]:
    return filter(lambda s: value in s, data)


def query_map(data: Union[Iterator[str], Iterable[str]], value: str) -> Iterator[str]:
    return map(lambda s: s.split()[int(value)], data)


def query_unique(data: Union[Iterator[str], Iterable[str]], value: Any) -> Iterable[str]:
    return set(data)


def query_sort(data: Union[Iterator[str], Iterable[str]], value: str) -> Iterable[str]:
    if value not in ["asc", "desc"]:
        raise ValueError("Wrong sort value")
    return sorted(data, reverse=value == "desc")


def query_limit(data: Union[Iterator[str], Iterable[str]], value: str) -> Iterator[str]:
    return map(itemgetter(0), zip(data, range(int(value))))


def query_regex(data: Union[Iterator[str], Iterable[str]], value: str) -> Iterator[str]:
    regex = re.compile(value)
    return filter(lambda s: regex.search(s), data)
