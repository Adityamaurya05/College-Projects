import tkinter as tk
import requests

# Define currency codes
currency_codes = {
    "USD": "United States Dollar",
    "INR": "Indian Rupee",
    "EUR": "Euro",
    "GBP": "British Pound",
    "JPY": "Japanese Yen",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CHF": "Swiss Franc",
    "CNY": "Chinese Yuan Renminbi",
    "HKD": "Hong Kong Dollar",
    "NZST": "New Zealand Dollar",
}

# Function to convert currency
def convert_currency():
    try:
        # Get user input
        from_currency = from_currency_entry.get().upper()
        to_currency = to_currency_entry.get().upper()
        amount = float(amount_entry.get())

        # Check for valid currency codes
        if from_currency not in currency_codes or to_currency not in currency_codes:
            raise ValueError(f"Invalid currency code(s).")

        # API endpoint
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

        # Send request
        response = requests.get(url)

        # Check for successful response
        if response.status_code == 200:
            data = response.json()

            # Get exchange rate
            exchange_rate = data["rates"][to_currency]

            # Calculate converted amount
            converted_amount = amount * exchange_rate

            # Format and display output
            converted_amount_label["text"] = f"{amount} {currency_codes[from_currency]} = {converted_amount:.2f} {currency_codes[to_currency]}"
        else:
            raise Exception(f"API request failed with status code {response.status_code}.")
    except ValueError as error:
        # Handle input errors
        converted_amount_label["text"] = f"Error: {error}"
    except Exception as error:
        # Handle unexpected errors
        converted_amount_label["text"] = f"Error: {error}. Please try again later."

# Create the main window
window = tk.Tk()
window.title("Currency Exchange")

# Create labels and entries
from_currency_label = tk.Label(window, text="From Currency:")
from_currency_entry = tk.Entry(window)
to_currency_label = tk.Label(window, text="To Currency:")
to_currency_entry = tk.Entry(window)
amount_label = tk.Label(window, text="Amount:")
amount_entry = tk.Entry(window)

# Create button and label for output
convert_button = tk.Button(window, text="Convert", command=convert_currency)
converted_amount_label = tk.Label(window, text="", font=("Arial", 12, "bold"))

# Place widgets on the window
from_currency_label.grid(row=0, column=0)
from_currency_entry.grid(row=0, column=1)
to_currency_label.grid(row=1, column=0)
to_currency_entry.grid(row=1, column=1)
amount_label.grid(row=2, column=0)
amount_entry.grid(row=2, column=1)
convert_button.grid(row=3, columnspan=2)
converted_amount_label.grid(row=4, columnspan=2)

# Run the main loop
window.mainloop()
