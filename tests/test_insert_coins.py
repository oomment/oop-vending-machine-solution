"""
Tests the insert_coins function.
"""
import pytest

from vending_machine import insert_coin


def test_invalid_coin_value():
    """
    When given a bogus coin value, raise a ValueError.
    """
    with pytest.raises(ValueError):
        insert_coin(99, [])


def test_five_cents():
    """Tests 5 cents being entered into machine."""
    inserted_coins = []
    insert_coin(5, inserted_coins)
    assert inserted_coins == [5]


def test_ten_cents():
    """Tests 10 cents being entered into machine."""
    inserted_coins = []
    insert_coin(10, inserted_coins)
    assert inserted_coins == [10]


def test_25_cents():
    """Tests 25 cents being entered into machine."""
    inserted_coins = []
    insert_coin(25, inserted_coins)
    assert inserted_coins == [25]


def test_100_cents():
    """Tests 100 cents being entered into machine."""
    inserted_coins = []
    insert_coin(100, inserted_coins)
    assert inserted_coins == [100]


def test_200_cents():
    """Tests 200 cents being entered into machine."""
    inserted_coins = []
    insert_coin(200, inserted_coins)
    assert inserted_coins == [200]
