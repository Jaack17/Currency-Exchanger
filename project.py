import requests

def main():
    api_key = "c5665de723eb464485c033120dc19db8"
    exchange_rates = fetch_exchange_rates(api_key)

    if not exchange_rates:
        print("Failed to retrieve exchange rates. Check your API key and endpoint.")
        return

    while True:
        try:
            source_amount = float(input("Enter the amount in the source currency: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid numerical amount.")

    source_currency = get_user_input("Enter the source currency (e.g., USD): ", exchange_rates)
    target_currency = get_user_input("Enter the target currency (e.g., EUR): ", exchange_rates)

    conversion_rate = exchange_rates[target_currency] / exchange_rates[source_currency]
    converted_amount = source_amount * conversion_rate

    print(f"{source_amount} {source_currency} is equivalent to {converted_amount} {target_currency}")

    while True:
        update_choice = input("Do you want to update exchange rates? (yes/no): ").strip().lower()
        if update_choice == "yes":
            exchange_rates = fetch_exchange_rates(api_key)
            if not exchange_rates:
                print("Failed to update exchange rates. Check your API key and endpoint.")
            else:
                print("Exchange rates updated.")
            break
        elif update_choice == "no":
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

def fetch_exchange_rates(api_key):
    api_url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
    response = requests.get(api_url)
    return response.json().get("rates", {})

def get_user_input(prompt, valid_currencies=None):
    while True:
        user_input = input(prompt).strip().upper()
        if not valid_currencies or user_input in valid_currencies:
            return user_input
        print("Invalid currency. Please try again.")

if __name__ == "__main__":
    main()












