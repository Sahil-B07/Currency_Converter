def main():
    currencyDict = {}
    with open('currency.txt') as f:
        lines = f.readlines()

    for line in lines:
        parsed = line.split("\t")

        currencyDict[parsed[0]] = parsed[1]

    amount = int(input("\nEnter amount: "))


    print("Enter a currency you want to convert in and\nThe Availabe options are (copy the name of respective currency and paste it.):\n")

    [print(currency) for currency in currencyDict.keys()]
    convert_to = input("\nPlease enter the name of currency : ")

    print(f"\n{amount} INR is equal to {amount * float(currencyDict[convert_to])} {convert_to}'s")


if __name__ == '__main__':
    main()
    while True:
        yNo = input("\nDo you want to continue(Y/n): ")
        if (yNo == "y" or yNo == "Y"):
            main()
        else:
            print("Thank you for using our Currency Converter!")
            break