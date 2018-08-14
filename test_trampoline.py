

import pytest
from contextlib import contextmanager

from trampoline import trampoline, TailCall


def test_simple():
    before, after = 0, 0
    def count(n):
        nonlocal before, after
        if n <= 0:
            return
        before += 1
        yield count(n - 1)
        after += 1

    trampoline(count(30))

    assert before == 30
    assert after == 30


def test_not_a_generator_error_none():
    with pytest.raises(TypeError):
        trampoline(None)


def test_not_a_generator_number():
    with pytest.raises(TypeError):
        trampoline(2)


class CtxCounter(object):

    def __init__(self):
        self.enters, self.exits, self.errors = 0, 0, 0

    def values(self):
        return self.enters, self.exits, self.errors

    @contextmanager
    def counting(self):
        self.enters += 1
        try:
            yield
        except:
            self.errors += 1
            raise
        finally:
            self.exits += 1


def test_contextmanager():
    counter = CtxCounter()
    inner_counts = None

    def count(n):
        nonlocal inner_counts
        if n <= 0:
            inner_counts = counter.values()
            return
        with counter.counting():
            yield count(n - 1)

    trampoline(count(30))

    assert inner_counts == (30, 0, 0)
    assert counter.values() == (30, 30, 0)


def test_tailcall_contextmanager():
    """Raise TailCall inside a contextmanager.

    Raising TailCall inside the contextmanager exits it immediately like any
    other exception. This is probably not what the user would want (probably
    invalid use of tail calls), but there may be valid uses for this.
    """

    counter = CtxCounter()
    inner_counts = None

    def count(n):
        nonlocal inner_counts
        if n <= 0:
            inner_counts = counter.values()
            return
        with counter.counting():
            raise TailCall(count(n - 1))
        yield

    trampoline(count(30))

    assert inner_counts == (30, 30, 30)
    assert counter.values() == (30, 30, 30)


def thrower():
    raise ValueError("Test")
    yield


def test_ignored_exception_result():

    def call_thrower():
        try:
            yield thrower()
        except ValueError:
            return "the_value"
        return "error"

    res = trampoline(call_thrower())

    assert res == "the_value"


def test_ignored_exception_recursion():

    def give_value():
        return "the_value"
        yield

    def call_thrower():
        try:
            yield thrower()
        except ValueError:
            return (yield give_value())
        return "error"

    res = trampoline(call_thrower())

    assert res == "the_value"


# vim:set sw=4 et:
