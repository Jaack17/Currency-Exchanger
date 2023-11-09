# Currency Exchange Program

This is a Python program that allows users to convert currency using the latest exchange rates from the Open Exchange Rates API. The program fetches exchange rates from the API, prompts the user for input, performs the currency conversion, and displays the result.

#### Video Demo:  <URL HERE>

## Files

- `project.py`: The main program file. It contains the code to interact with the user, fetch exchange rates, and perform currency conversion.

## Description

1. The program starts by fetching the latest exchange rates from the Open Exchange Rates API using your API key.

2. It then prompts the user for the following information:
   - The amount in the source currency they want to convert.
   - The source currency (e.g., USD).
   - The target currency (e.g., EUR).

3. The program validates user input for currencies and numerical amounts.

4. It calculates the converted amount using the provided exchange rates and displays the result to the user.

5. The user has the option to update exchange rates if needed. If they choose to update, the program will fetch the latest rates from the API.

6. After completing the currency exchange, the user can decide whether to exchange currency again or exit the program.

## Design Choices

- The program uses clear and concise prompts to guide the user through the currency conversion process.

- It provides error handling for various scenarios, such as invalid input and API-related errors.

- The code is organized into functions to improve readability and maintainability.

- The program allows users to update exchange rates if they suspect outdated information.

## Usage

1. Before running the program, obtain an API key from [Open Exchange Rates](https://openexchangerates.org/signup) and replace the `api_key` variable in the code.

2. Run the program using Python: `python project.py`

3. Follow the prompts to convert currency, update exchange rates, and exchange currency again.

## Author

- Giacomo Innocenti

## License

This project is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for details.

## Acknowledgments

- The program uses data from the Open Exchange Rates API.

