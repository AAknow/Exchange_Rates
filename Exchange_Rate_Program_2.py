## CST-16163 Intro to Computer Programming
## By: Aaron Knowles

def main():
    exchList = convertToList("Exchrate.txt")
    numList = convertToNumList(exchList)
    # loops through numList and prints exchList equivalent
    for num in numList:
        for index in exchList:
            if str(num) == index[2]:
                print(index[0])
                # removes entry so other entries with same value can be printed
                exchList.remove(index)
                break

def convertToList(filename):
    infile = open(filename)
    extractList = [line.rstrip() for line in infile]
    infile.close()
    newList = []
    # converts each line into a list and adds it to newList
    for line in extractList:
        newList.append(line.split(","))
    return newList

def convertToNumList(exchList):
    numList = []
    # takes the exchange rates and add them to num list
    for index in exchList:
        numList.append(eval(index[2]))
    # sorts the list so numbers are in ascending order
    numList.sort()
    return numList

main()
    
    
