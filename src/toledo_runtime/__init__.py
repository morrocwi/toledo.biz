"""Toledo Citizen Platform reference runtime.

Product implementation lives here; mathematical authority remains upstream in
https://github.com/morrocwi/toledo.
"""

from .equations import EquationStore
from .institutions import InstitutionStore
from .protocol import compile_protocol, validate_handoff, validate_return_gate

__all__ = [
    "EquationStore",
    "InstitutionStore",
    "compile_protocol",
    "validate_handoff",
    "validate_return_gate",
]

__version__ = "0.2.1"
