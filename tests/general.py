"""This file tests the functionality of the classes."""

# Dependencies

# Main Classes
from classes.portfolio import Portfolio
from classes.stock import Stock


# Calculate Profit of a single Stock
def test_single_stock_profit():
    """Test the profit of a single stock."""
    # Create a single stock
    stock = Stock({'2019-01-01': 10, '2019-01-02': 20})

    # Create a portfolio with the stock
    portfolio = Portfolio([stock])

    # Calculate the profit
    profit = portfolio.profit('2019-01-01', '2019-01-02')

    # Check the profit
    assert profit == 10


# Calculate Profit of a portfolio with multiple stocks
def test_multiple_stock_profit():
    """Test the profit of a portfolio with multiple stocks."""
    # Declare dates
    date_start = '2019-01-01'
    date_end = '2019-01-02'

    # Create a group of stocks
    stocks = [
        Stock({date_start: 10, date_end: 20}) for _ in range(3)
    ]

    # Create a portfolio with the stock
    portfolio = Portfolio(stocks)

    # Calculate the profit
    profit = portfolio.profit(date_start, date_end)

    # Check the profit
    assert profit == 20


# Calculate Annualized return of a portfolio with a single stock
def test_single_stock_annualized_return():
    """Test the annualized return of a single stock."""
    # Create a single stock
    stock = Stock({'2019-01-11': 10, '2020-12-16': 20})

    # Create a portfolio with the stock
    portfolio = Portfolio([stock])

    # Calculate the profit
    annualized_return = portfolio.getAnnualizedReturn('2019-01-11', '2019-12-16')

    # Check the profit
    assert annualized_return == 0.5


# Caclulate Annualized returnt of a portfolio with multiple stocks
def test_multiple_stock_annualized_return():
    """Test the annualized return of a portfolio with multiple stocks."""
    # Declare dates
    date_start = '2019-01-11'
    date_end = '2020-12-16'

    # Create a group of stocks
    stocks = [
        Stock({date_start: 10, date_end: 20}) for _ in range(3)
    ]

    # Create a portfolio with the stock
    portfolio = Portfolio(stocks)

    # Calculate the profit
    annualized_return = portfolio.getAnnualizedReturn(date_start, date_end)

    # Check the profit
    assert annualized_return == 0.5
