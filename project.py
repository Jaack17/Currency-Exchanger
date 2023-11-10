import requests

def main():
    api_key = "c5665de723eb464485c033120dc19db8"

    # Fetch currency names from the API
    valid_currencies = fetch_currency_names(api_key)

    while True:
        exchange_rates = fetch_exchange_rates(api_key)
        
        if not exchange_rates or not valid_currencies:
            print("Failed to retrieve exchange rates or currency names. Please check your API key and endpoint.")
            return

        source_amount = get_source_amount()
        source_currency = get_user_input("Enter the source currency: ", valid_currencies)
        target_currency = get_user_input("Enter the target currency: ", valid_currencies)

        conversion_rate = exchange_rates[target_currency] / exchange_rates[source_currency]
        converted_amount = source_amount * conversion_rate

        print(f"\n{source_amount} {source_currency} is equivalent to {converted_amount:.2f} {target_currency}\n")

        if not update_exchange_rates(api_key):
            print("Failed to update exchange rates. Please check your API key and endpoint.")
            return

        if not exchange_currency_again():
            print("Thank you for using my currency converter. Goodbye!")
            break

# Function to fetch currency names
def fetch_currency_names(api_key):
    # Fetch the latest exchange rates from the Open Exchange Rates API
    api_url = f"https://openexchangerates.org/api/currencies.json?app_id={api_key}"
    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve currency names. Please check your API key and endpoint.")
        return {}

# Function to fetch exchange rates
def fetch_exchange_rates(api_key):
    api_url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    response = requests.get(api_url)
    return response.json().get("rates", {})

# Function to get the source amount from the user
def get_source_amount():
    while True:
        try:
            source_amount = float(input("Enter the amount in the source currency: "))
            return source_amount
        except ValueError:
            print("Invalid input. Please enter a valid numerical amount.")

# Function to get user input for currency selection
def get_user_input(prompt, valid_currencies=None):
    while True:
        user_input = input(prompt).strip().upper()

        # Check if the input is a valid currency code
        if not valid_currencies or user_input in valid_currencies:
            return user_input
        else:
            # Check if the input matches a currency symbol or name
            for code, name in valid_currencies.items():
                if (
                    user_input == code
                    or user_input == name.upper()
                    or user_input == name.lower()
                    or user_input in name.upper().split(" ")
                    or user_input in name.lower().split(" ")
                    or user_input == get_currency_symbol(code)
                ):
                    return code

            print("Invalid currency. Please enter a valid currency code, symbol, or name.")

# Function to get currency symbol
def get_currency_symbol(currency_code):
    # Add more symbols as needed
    symbol_map = {
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "JPY": "¥",
    }
    return symbol_map.get(currency_code, "")

# Example: If the user types "$", it will be recognized as valid for USD.

# Function to update exchange rates
def update_exchange_rates(api_key):
    while True:
        update_choice = input("Do you want to update exchange rates? (yes/no): ").strip().lower()
        if update_choice == "yes":
            new_rates = fetch_exchange_rates(api_key)
            if new_rates:
                print("Exchange rates updated successfully.\n")
                return True
            else:
                print("Failed to update exchange rates. Please check your API key and endpoint.")
        elif update_choice == "no":
            return True
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

# Function to ask if the user wants to exchange currency again
def exchange_currency_again():
    while True:
        update_choice = input("Do you want to exchange currency again? (yes/no): ").strip().lower()
        if update_choice == "no":
            return False
        elif update_choice == "yes":
            return True
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()


















