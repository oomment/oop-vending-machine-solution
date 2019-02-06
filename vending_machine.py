"""
A virtual vending machine.
"""
def insert_coins(coin):
    """Inserts coins."""
    raise ValueError


class InsufficientFunds(Exception):
    """
    Exception used to indicate that there isn't
    enough money to make a purchase.
    """
