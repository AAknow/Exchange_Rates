def main():
    exchList = convertToList("Exchrate.txt")
    inputCheck = 0
    while inputCheck == 0:
        country = input("Enter the name of a country: ")
        # check if input is in list
        for index in exchList:
            if index[0] == country.title():
                print("Currency: " + index[1] + "\nExchange Rate: " + index[2])
                inputCheck = 1
            # if input check hasn't changed and the loop is on its last pass
            elif index == exchList[-1] and inputCheck == 0:
                print("\nPlease enter a valid country.\n")
    
def convertToList(filename):
    infile = open(filename)
    extractList = [line.rstrip() for line in infile]
    infile.close()
    newList = []
    # converts each line into a list and adds it to newList
    for line in extractList:
        newList.append(line.split(","))
    return newList

main()
    

