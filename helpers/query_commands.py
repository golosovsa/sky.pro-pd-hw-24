"""
    query filter
"""
from operator import itemgetter


def query_filter(data, value):
    return filter(lambda s: value in s, data)


def query_map(data, value):
    return map(lambda s: s.split()[int(value)], data)


def query_unique(data, value):
    data_uniq = set()
    for item in data:
        if item not in data_uniq:
            data_uniq.add(item)
            yield item


def query_sort(data, value):
    assert value in ["asc", "desc"], "Wrong sort value"
    return sorted(data, reverse=value == "desc")


def query_limit(data, value):
    return map(itemgetter(0), zip(data, range(int(value))))
