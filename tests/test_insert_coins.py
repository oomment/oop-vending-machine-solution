"""
Tests the insert_coins function.
"""
import pytest

from vending_machine import insert_coins


def test_invalid_coin_value():
    """
    When given a bogus coin value, raise a ValueError.
    """
    with pytest.raises(ValueError):
        insert_coins(99)
