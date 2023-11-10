from unittest.mock import patch, Mock
from project import (
    fetch_exchange_rates,
    get_source_amount,
    get_user_input,
    update_exchange_rates,
    exchange_currency_again,
)

def test_get_user_input_valid():
    with patch('builtins.input', return_value="USD"):
        assert get_user_input("Enter a currency code: ") == "USD"

def test_get_user_input_invalid():
    with patch('builtins.input', side_effect=["InvalidCurrency", "USD"]):
        assert get_user_input("Enter a currency code: ") == "INVALIDCURRENCY"

def test_get_source_amount():
    with patch('builtins.input', return_value="100"):
        assert get_source_amount() == 100.0

def test_update_exchange_rates_yes():
    with patch('builtins.input', return_value="yes"):
        with patch('project.fetch_exchange_rates', return_value={"USD": 1.0}):
            assert update_exchange_rates("test_api_key") is True

def test_update_exchange_rates_no():
    with patch('builtins.input', return_value="no"):
        assert update_exchange_rates("test_api_key") == True

def test_exchange_currency_again_yes():
    with patch('builtins.input', return_value="yes"):
        assert exchange_currency_again() == True

def test_exchange_currency_again_no():
    with patch('builtins.input', return_value="no"):
        assert exchange_currency_again() == False

def test_fetch_exchange_rates():
    api_key = "test_api_key"
    expected_rates = {"USD": 1.0, "EUR": 0.85, "GBP": 0.75, "JPY": 110.0}
    with patch('project.requests.get', return_value=Mock(json=lambda: {"rates": expected_rates})):
        actual_rates = fetch_exchange_rates(api_key)

    assert actual_rates == expected_rates

