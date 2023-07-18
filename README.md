# learn.py

Code and Notes for Python Language.

<br>

## Utilities
<br>

- `AttrDict`: a mapping that allows attribute-style access, key-style access, and double star `**` unpacking.
  - Usage:
    ```python
    from dictionary import AttrDict

    d = AttrDict(a = 1, b = 2)
    assert d.a == d['a']
    ```

- `show`: Compactly display the structure of an arbitrary object, like a dict, a list, etc.
  - Usage:
    ```python
    from structure import Show

    x = {i: list(range(100)) for i in range(100)}
    show = Show(max_len=10, indent='..')
    show(x)
    ```

<br>
