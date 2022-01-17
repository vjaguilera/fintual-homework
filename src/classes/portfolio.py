"""This file containes the Portfolio class."""

# Dependencies
from functools import reduce
from typing import List
from datetime import datetime

# Interfaces
from ..interfaces.stock import IStock

# Constants
from ..const import N_DAYS_YEAR

# Helpers
from ..helpers import percentage


class Portfolio:
    def __init__(self, stocks: List[IStock]) -> None:
        self.stocks = stocks

    def getDaysDiff(self, date_start: str, date_end: str) -> int:
        """Return the number of days between the two dates."""
        # References:
        # - https://stackoverflow.com/questions/8419564/difference-between-two-dates-in-python
        date_start_format = datetime.strptime(date_start, "%Y-%m-%d")
        date_end_format = datetime.strptime(date_end, "%Y-%m-%d")
        return abs((date_end_format - date_start_format).days)

    @percentage
    def getAnnualizedReturn(self, date_start: str, date_end: str, percentage=False) -> float:
        """Return the annualized return of the portfolio on the given date."""
        # Annualized Return:
        # - https://scripbox.com/pf/annualized-return/
        # - https://corporatefinanceinstitute.com/resources/knowledge/trading-investing/annual-return/
        # - https://www.investopedia.com/terms/a/annualized-total-return.asp

        # Investopedia talks about Cummulative Return to calculate Annualized Return
        #  https://www.investopedia.com/terms/c/cumulativereturn.asp

        days_held = self.getDaysDiff(date_start, date_end)
        date_start_profit = reduce(
            lambda accum, diff: accum + diff, [stock.price(date_start) for stock in self.stocks], 0)
        date_end_profit = reduce(
            lambda accum, diff: accum + diff, [stock.price(date_end) for stock in self.stocks], 0)

        # Cummulative Return = Current Value - Original Value / Original Value
        cummulative_return = (date_end_profit - date_start_profit) / date_start_profit

        # Annualized Return = (1 + Cummulative Return) ^ (365 / Days Held) - 1
        # OBS: Declare 365 as a var to avoid MAGIC NUMBERS
        annualized_return = (1 + cummulative_return) ** (N_DAYS_YEAR / days_held) - 1
        return annualized_return

    def profit(self, date_start: str, date_end: str, annualized=False, percentage=False) -> float:
        """Return the revenue of the portfolio on the given date."""
        if annualized:
            return self.getAnnualizedReturn(date_start, date_end, percentage)
        return reduce(
            lambda accum, diff: accum + diff,
            [stock.price(date_end) - stock.price(date_start) for stock in self.stocks], 0)

    def appendStock(self, stock: IStock) -> None:
        """Append a stock to the portfolio."""
        self.stocks.append(stock)
