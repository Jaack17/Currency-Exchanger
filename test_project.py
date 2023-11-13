import pytest
from project import fetch_currency_names, fetch_exchange_rates, get_currency_symbol

@pytest.fixture
def mock_fetch_currency_names(requests_mock):
    requests_mock.get("https://openexchangerates.org/api/currencies.json", json={"USD": "United States Dollar", "EUR": "Euro"})
    return fetch_currency_names("fake_api_key")

@pytest.fixture
def mock_fetch_exchange_rates(requests_mock):
    requests_mock.get("https://openexchangerates.org/api/latest.json", json={"rates": {"USD": 1.0, "EUR": 0.85}})
    return fetch_exchange_rates("fake_api_key")

def test_fetch_currency_names(mock_fetch_currency_names):
    assert mock_fetch_currency_names == {"USD": "United States Dollar", "EUR": "Euro"}

def test_fetch_exchange_rates(mock_fetch_exchange_rates):
    assert mock_fetch_exchange_rates == {"USD": 1.0, "EUR": 0.85}

def test_get_currency_symbol():
    assert get_currency_symbol("USD") == "$"
    assert get_currency_symbol("GBP") == "£"
    assert get_currency_symbol("XYZ") == ""




