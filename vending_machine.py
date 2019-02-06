"""
A virtual vending machine.
"""
def insert_coin(coin, inserted_coins):
    """Inserts coin."""
    valid_coins = [5, 10, 25, 100, 200]
    if coin in valid_coins:
        inserted_coins.append(coin)
    else:
        raise ValueError


class InsufficientFunds(Exception):
    """
    Exception used to indicate that there isn't
    enough money to make a purchase.
    """
