import sys
import requests

if not len(sys.argv) == 2:
    sys.exit("Missing command-line argument")

try:
    n  =  sys.argv[1]
    n = float(n)
except ValueError:
    sys.exit("Command-line argument is not a number")
try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=dcd125e0680d9ba372253b5333e30edc96e8d440ddea06edf72860f75bac4bb8")
except requests.RequestException:
    sys.exit("Error in request")
o = response.json()
price = o["data"]["priceUsd"]
price = float(price)
amount = n * price
print(f"${amount:,.4f}")
