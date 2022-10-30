"""
Implements RegEx abstraction logic, for easy working with RegEx in Python.
"""
__title__ = "remagic"
__version__ = "0.1.1"
__author__ = "ificiana"
__license__ = "MIT License"
__copyright__ = "Copyright 2022 ificiana"

import sys

from .constants import Consts
from .interface import (
    after,
    any_of,
    before,
    char_in,
    char_not_in,
    create,
    exactly,
    not_after,
    not_before,
    one_or_more,
    optional,
    ref,
    zero_or_more,
)

if sys.version_info >= (3, 8):  # pragma: no cover
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata  # pragma: no cover


def get_version() -> str:
    try:
        return str(importlib_metadata.version(__name__))
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()

CHAR = create(Consts.CHAR)
WHITESPACE = create(Consts.WHITESPACE)
NOT_WHITESPACE = create(Consts.NOT_WHITESPACE)
WS = create(Consts.WS)
NOT_WS = create(Consts.NOT_WS)
WORD = create(Consts.WORD)
NOT_WORD = create(Consts.NOT_WORD)
DIGIT = create(Consts.DIGIT)
NOT_DIGIT = create(Consts.NOT_DIGIT)
LETTER = create(Consts.LETTER)
NOT_LETTER = create(Consts.NOT_LETTER)
TAB = create(Consts.TAB)
NEWLINE = create(Consts.NEWLINE)
NOT_NEWLINE = create(Consts.NOT_NEWLINE)
CARRIAGE_RETURN = create(Consts.CARRIAGE_RETURN)
N = create(Consts.N)
NOT_N = create(Consts.NOT_N)
R = create(Consts.R)

__all__ = [
    "CARRIAGE_RETURN",
    "CHAR",
    "Consts",
    "DIGIT",
    "LETTER",
    "N",
    "NEWLINE",
    "NOT_DIGIT",
    "NOT_LETTER",
    "NOT_N",
    "NOT_NEWLINE",
    "NOT_WHITESPACE",
    "NOT_WORD",
    "NOT_WS",
    "R",
    "TAB",
    "WHITESPACE",
    "WORD",
    "WS",
    "after",
    "any_of",
    "before",
    "char_in",
    "char_not_in",
    "create",
    "exactly",
    "not_after",
    "not_before",
    "one_or_more",
    "optional",
    "version",
    "get_version",
    "zero_or_more",
    "ref",
]
