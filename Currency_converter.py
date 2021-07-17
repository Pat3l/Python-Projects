from forex_python.converter import CurrencyRates
c = CurrencyRates()

from_currency = input("From currency: ").upper()
to_currency = input("To currency: ").upper()
amount = int(input("Enter the amount: "))

result = c.convert(from_currency, to_currency, amount)
print(f"Conversion of {amount} from {from_currency} to {to_currency} is {result}.")

