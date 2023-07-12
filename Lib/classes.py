__all__ = ['add_to_class', 'SaveArgs']

import inspect

# Copied from the book Dive into Deep Learning (d2l.ai) by Zhang et al.
def add_to_class(Class):
    '''Register functions as methods in the given class.'''
    def wrapper(obj):
        setattr(Class, obj.__name__, obj)
    return wrapper

# Modified from the book Dive into Deep Learning (d2l.ai) by Zhang et al.
class SaveArgs:
    def save_args(self, ignore=()):
        '''Save arguments as object attributes.'''
        local_vars = inspect.currentframe().f_back.f_locals
        for k in local_vars:
            if not k.startswith('_') and k not in ('self', *ignore):
                setattr(self, k, local_vars[k])
