"""
    Main
"""
from pathlib import Path
from typing import Iterator, Union, Tuple, Iterable, Dict, Callable

from helpers import ServerError, create_file_gen, \
    query_filter, query_map, query_unique, query_sort, query_limit, query_regex
from constants import DATA_DIR

COMMANDS: Dict[str, Callable[[Union[Iterator[str], Iterable[str]], str], Union[Iterator[str], Iterable[str]]]] = {
    "filter": query_filter,
    "map": query_map,
    "unique": query_unique,
    "sort": query_sort,
    "limit": query_limit,
    "regex": query_regex,
}


def _compile_query(
        extracted_commands: Iterator[Tuple[str, str]],
        incoming_data: Union[Iterator[str], Iterable[str]]) -> Union[Iterator[str], Iterable[str]]:
    iterator = incoming_data
    for cmd, value in extracted_commands:
        iterator = COMMANDS[cmd](iterator, value)
    return iterator


def _assert_path(path: Path):
    if DATA_DIR not in path.parents:
        raise ValueError("You are trying to hack the server... It won't work)))")
    if not path.is_file():
        raise FileNotFoundError("Wrong filename")
    if not path.exists():
        raise FileExistsError("File does not exist")


def _extract_commands(data: dict) -> Iterator[Tuple[str, str]]:
    keys = sorted(data.keys())
    cmds = (data[key] for key in keys if key.startswith("cmd"))
    values = (data[key] for key in keys if key.startswith("value"))
    return zip(cmds, values)


def setup_query(data: dict) -> Union[Iterator[str], Iterable[str]]:
    try:
        filename: str = data["file_name"]
        path = DATA_DIR.joinpath(filename).resolve()
        _assert_path(path)
        file_iterator = create_file_gen(path)
        extracted_commands = _extract_commands(data)
        result = _compile_query(extracted_commands, file_iterator)

        return result
    except (KeyError,
            ValueError,
            AssertionError,
            TypeError,
            FileNotFoundError,
            FileExistsError,) as error:
        raise ServerError(str(error))
