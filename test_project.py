import pytest
from project import fetch_exchange_rates, get_user_input, main

def test_fetch_exchange_rates():

    api_key = "c5665de723eb464485c033120dc19db8"
    exchange_rates = fetch_exchange_rates(api_key)
    assert isinstance(exchange_rates, dict)
    assert len(exchange_rates) > 0

def test_get_user_input():
    valid_currencies = ["USD", "EUR", "GBP", "JPY"]

    with pytest.raises(StopIteration):
        user_input = iter(["USD"])
        assert get_user_input("Enter a currency code: ", valid_currencies, input_func=lambda _: next(user_input))

    with pytest.raises(StopIteration):
        user_input = iter(["AUD", "USD"])
        assert get_user_input("Enter a currency code: ", valid_currencies, input_func=lambda _: next(user_input))

def test_main():
    source_currency = "USD"
    target_currency = "EUR"
    exchange_rates = {"USD": 1.0, "EUR": 0.85, "GBP": 0.75, "JPY": 110.0}
    source_amount = 100
    result = main(source_currency, target_currency, source_amount, exchange_rates)
    assert result == 85.0

