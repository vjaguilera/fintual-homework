"""This file contains the Stock class."""

# Dependencies
from typing import Dict


class Stock:
    def __init__(self, date_values: Dict) -> None:
        """Initialize a Stock object.
            - date_values: A dictionary of dates and their corresponding values.
        """
        self.date_values = date_values

    def price(self, date: str) -> float:
        """Return the price of the stock on the given date."""
        return self.date_values.get(date, 0)
