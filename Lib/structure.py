__all__ = ['Show']

import re
from typing import Optional
from classes import SaveArgs

def get_type(x) -> str:
    _type = str(type(x))
    return re.match("<class '(.+)'>", _type).groups()[0]

def add_hier(string: str, indent: str = '..') -> str:
    if string:
        _elem = [indent + line for line in string.split('\n')]
        return '\n'.join(_elem)
    else:
        return string

class Show(SaveArgs):
    def __init__(self, max_len: Optional[int] = None, indent: str = '..',
                 max_len_dict: int = 10, max_len_list: int = 10, call: bool = True) -> None:
        self.save_args()
        if self.max_len:
            self.max_len_dict = self.max_len
            self.max_len_list = self.max_len

    def __call__(self, x) -> Optional[str]:
        if isinstance(x, dict):
            return Dict.show(x, self.max_len, self.indent,
                             self.max_len_dict, self.max_len_list, self.call)
        elif isinstance(x, (tuple, list, set)):
            return List.show(x, self.max_len, self.indent,
                             self.max_len_dict, self.max_len_list, self.call)
        else:
            return print(x) if self.call else repr(x)

class Dict(dict):
    def show(x, max_len: Optional[int] = None, indent: str = '..',
             max_len_dict: int = 10, max_len_list: int = 10, call: bool = True) -> Optional[str]:
        show = Show(max_len, indent, max_len_dict, max_len_list, call=False)
        _len = len(x)
        _type = get_type(x)
        _elem = '\n'.join([show(k) + ': ' + show(v)
                            for k, v in list(x.items())[:max_len_dict]])
        if _len > max_len_dict:
            _elem += '\n(structure output truncated)'
        output = f'A {_type} of {_len}:\n{add_hier(_elem, indent)}'
        return print(output) if call else output

class List(list):
    def show(x, max_len: Optional[int] = None, indent: str = '..',
             max_len_dict: int = 10, max_len_list: int = 10, call: bool = True) -> Optional[str]:
        show = Show(max_len, indent, max_len_dict, max_len_list, call=False)
        _len = len(x)
        _type = get_type(x)
        _elem = ' '.join([show(i) for i in list(x)[:max_len_list]])
        if _len > max_len_list:
            _elem += ' ... '
        output = f'[A {_type} of {_len}: {_elem}]'
        return print(output) if call else output
    
