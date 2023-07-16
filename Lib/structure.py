__all__ = ['show']

import re
from typing import Union

def show(x, call: bool = True) -> Union[str, None]:
    if isinstance(x, dict):
        return Dict.show(x, call)
    elif isinstance(x, (tuple, list, set)):
        return List.show(x, call)
    else:
        return print(x) if call else repr(x)

def get_type(x) -> str:
    _type = str(type(x))
    return re.match("<class '(.+)'>", _type).groups()[0]

def add_hier(string: str, prefix: str = "..") -> str:
    _elem = [prefix + line for line in string.split('\n')]
    return '\n'.join(_elem)

class Dict(dict):
    def show(x, call: bool = True, max_len: int = 10) -> Union[str, None]:
        _len = len(x)
        _type = get_type(x)
        _elem = "\n".join([show(k, call=False) + ": " + show(v, call=False)
                            for k, v in list(x.items())[:max_len]])
        if _len > max_len:
            _elem += "\n(structure output truncated)"
        output = f"A {_type} of {_len}:\n{add_hier(_elem)}"
        return print(output) if call else output

class List(list):
    def show(x, call: bool = True, max_len: int = 10) -> Union[str, None]:
        _len = len(x)
        _type = get_type(x)
        _elem = " ".join([show(i, call=False) for i in list(x)[:max_len]])
        if _len > max_len:
            _elem += " ... "
        output = f"[A {_type} of {_len}: {_elem}]"
        return print(output) if call else output

