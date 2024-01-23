import requests
import sys
def main():
    if len(sys.argv) != 2:
        print("Command-line argument is not a number")
        sys.exit(1)
    else:
        bitcoin_amount = sys.argv[1]
        get_bitcoin_value_in_usd(bitcoin_amount)

def get_bitcoin_value_in_usd(bitcoin_amount):
    try:
        bitcoin_amount = float(bitcoin_amount)
        if bitcoin_amount < 0:
            print("Missing command-line argument")
            return

        # API URL for current Bitcoin price in USD
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"

        # Send GET request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            usd_price = data["bpi"]["USD"]["rate_float"]
            value_in_usd = (bitcoin_amount * usd_price)
            print(f"${value_in_usd:,.4f}")
        else:
            print("Failed to fetch Bitcoin data from the API.")
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)

if __name__ == "__main__":
    main()

#TODO output of bitcoin value should be to 4 decimal places and uses , as a float seperator
