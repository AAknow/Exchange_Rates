def main():
    exchDict = convertToDictionary("Exchrate.txt")
    # run loop until break is called
    while True:
        countryOne = input("Enter the name of the first country: ")
        countryTwo = input("Enter the name of the second country: ")
        # if inputs are in exchDict, get conversion and break loop
        if countryOne.title() in exchDict and countryTwo.title() in exchDict:
            rateOne = exchDict[countryOne.title()]["Rate"]
            rateTwo = exchDict[countryTwo.title()]["Rate"]
            conversion = calculateConversion(rateOne, rateTwo)
            break
        else:
            print("\nPlease input valid countries.\n")
    # print results
    print(conversion[1] + " " + exchDict[countryOne.title()]["Currency"] \
          + "s " + "from " + countryOne.title() + " equals " \
          + conversion[0] + " " + exchDict[countryTwo.title()]["Currency"] \
          + "s " + "from " + countryTwo.title())

def convertToDictionary(filename):
    infile = open(filename)
    extractList = [line.rstrip() for line in infile]
    infile.close()
    newDict = {}
    # converts each line into a list
    # creates a key value pair in newDict with a dictionary as the value
    for line in extractList:
        countryList = line.split(",")
        newDict[countryList[0]] = {"Currency" : countryList[1], \
                                   "Rate" : float(countryList[2])}
    return newDict

def calculateConversion(one, two):
    # run loop until break is called
    while True:
        amount = input("Enter amount of money to convert: ")
        # if amount is number, calculate conversion
        try:
            float(amount)
            conversion = float(amount) * (1/one) * two
            break
        except ValueError:
            print("\nPlease input a valid number.\n")
    return [str(round(conversion, 2)), amount]

main()
