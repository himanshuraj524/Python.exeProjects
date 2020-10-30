# Currency Converter
import time

# waitsec = time.sleep(0.100)

currencydict = {}  # empty currency dictionary.

with open("currencies.txt","r") as f:  # file of all the currency data.
    lines = f.readlines()
    for line in lines:
        parse = line.split("-")  # split the country name with exchange rate.
        currencydict[parse[0].lower()] = parse[1]  # append that parsed data into the currency dict as key and value.

if __name__ == "__main__":
    while True:
        print("\t\t\tWELCOME TO MY CURRENCY CONVERTER.\n")

        print("I Can Convert These Currencies - \n")

        # [print(item.upper(),waitsec) for item in currencydict.keys()]
        for item in currencydict.keys():
            print(item)
            time.sleep(0.1)

        currency = input("Enter the name of the currency to exchange from indian rupees-\n").lower()
        if currency not in currencydict:
            print("Please Enter A Valid currency.\n")
            continue
        else:
            try:
                amount = int(input("Enter the amount-\n"))
                print(f"{amount} INR is Equal to {amount * float(currencydict[currency])} {currency}\n")
                ext = input("Hit Enter To Convert Again or X For Exit.\n").lower()
                if ext != "x":
                    continue
                else:
                    break
            except ValueError as Error:
                print("Please Enter a digit to convert,try again-\n")
                continue
        break
