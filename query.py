"""
    Main
"""
from pathlib import Path
from helpers import ServerError, create_file_gen, \
    query_filter, query_map, query_unique, query_sort, query_limit
from constants import DATA_DIR


commands = {
    "filter": query_filter,
    "map": query_map,
    "unique": query_unique,
    "sort": query_sort,
    "limit": query_limit
}


def _compile_query(extracted_commands, incoming_data):
    it = incoming_data
    for cmd, value in extracted_commands:
        it = commands[cmd](it, value)
    return it


def _assert_path(path: Path):
    assert DATA_DIR in path.parents, "You are trying to hack the server... It won't work)))"
    assert path.is_file(), "Wrong filename"
    assert path.exists(), "File does not exist"


def _extract_commands(data: dict):
    keys = sorted(data.keys())
    cmds = (data[key] for key in keys if key.startswith("cmd"))
    values = (data[key] for key in keys if key.startswith("value"))
    return zip(cmds, values)


def setup_query(data: dict):
    try:
        filename: str = data["file_name"]
        path = DATA_DIR.joinpath(filename).resolve()
        _assert_path(path)
        file_iterator = create_file_gen(path)
        extracted_commands = _extract_commands(data)
        result = _compile_query(extracted_commands, file_iterator)

        return result
    except (KeyError, ValueError, AssertionError, TypeError, ) as error:
        raise ServerError(str(error))

