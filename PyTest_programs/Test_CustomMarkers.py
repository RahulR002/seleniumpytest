
import sys

import pytest


@pytest.mark.smoke
def test_1():
    x = 10
    y = 20
    assert x == y


@pytest.mark.regression
def test_2():
    x = 20
    y = 20
    assert x == y


@pytest.mark.smoke
@pytest.mark.regression
def test_3():
    x = 10
    y = 20
    result = x + y
    assert result == 30