"""DEPRECATED: Function signature objects for callables.

Use the standard library version if available, as it is more up to date.
Fallback on backport otherwise.
"""


import warnings
warnings.warn(
    f"{__name__} backport for Python 2 is deprecated in IPython 6, which only supports Python 3. Import directly from  standard library `inspect`",
    DeprecationWarning,
    stacklevel=2,
)

from inspect import BoundArguments, Parameter, Signature, signature
