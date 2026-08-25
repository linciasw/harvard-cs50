# https://pro.coincap.io/dashboard
# https://pro.coincap.io/api-docs/

# CoinCap documentation tells you what their API expects.
# requests documentation tells you how Python sends an HTTP request.
# CS50's specification tells you what your program is supposed to do.
# Your code is where you connect all three.


# You don't need to learn the entire library. Focus on these concepts:

# requests.get()
# URL parameters — params=
# HTTP headers — headers=
# Response objects
# response.status_code
# response.text
# response.json()
# Handling errors
# Reading JSON dictionaries/lists

# The official documentation is here:
# https://requests.readthedocs.io/en/latest/user/quickstart/?utm_source=chatgpt.com


# And pay particular attention to the sections "Passing Parameters In URLs", 
# "Response Content", "JSON Response Content", and "Custom Headers."

import sys
import requests



API_KEY = "acc97ed45d648a8fd5ac30c1e039c1a7420408e9b48076f38032f91f25d47475"


def main():


    print(sys.argv)

    if len(sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit()



    bitcoin = float(sys.argv[1])




    response= requests.get(
        "https://rest.coincap.io/v3/price/bysymbol/BTC",
        headers={"Authorization": f"Bearer {API_KEY}"}
    )


    data = response.json()
    price = float(data["data"][0])

    total = bitcoin * price 
    print(f"$ {total:,.2f}")

    # print("BTC:")
    # print(response.status_code)
    # print(response.text)






main()