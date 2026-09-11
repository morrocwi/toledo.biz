"""Toledo Citizen Platform reference runtime.

Product implementation lives here; mathematical authority remains upstream in
https://github.com/morrocwi/toledo.
"""

from .cases import (
    apply_case_event,
    case_to_compile_input,
    create_case_passport,
    evaluate_return_object,
    step_case,
)
from .equations import EquationStore
from .institutions import InstitutionStore
from .protocol import compile_protocol, validate_handoff, validate_return_gate

__all__ = [
    "EquationStore",
    "InstitutionStore",
    "compile_protocol",
    "validate_handoff",
    "validate_return_gate",
    "create_case_passport",
    "apply_case_event",
    "evaluate_return_object",
    "case_to_compile_input",
    "step_case",
]

__version__ = "0.4.0"
