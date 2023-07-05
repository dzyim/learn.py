__all__ = ['SaveArgs']

import inspect

class SaveArgs:
    def save_args(self, ignore=()):
        '''Save arguments as object attributes.'''
        local_vars = inspect.currentframe().f_back.f_locals
        for k in local_vars:
            if not k.startswith('_') and k not in ('self', *ignore):
                setattr(self, k, local_vars[k])
