print('Level 3 - Count characters in a string')


def countPerChar(strToCount):
    charCount = {}
    strToList = list(strToCount)
    strToList.sort(key=str.lower, reverse=True)
    while strToList:
        letterToTest = strToList.pop()
        if (letterToTest.strip()):
            if letterToTest in charCount:
                charCount[letterToTest] += 1
            else:
                charCount[letterToTest] = 1
    return charCount


def countPerCharCaseless(strToCount):
    return countPerChar(strToCount.upper())


strToCount = 'Row Row Row Your Boat'
print("Case Sensetive Count Per Charaster:")
print(countPerChar(strToCount))
print("\n Caseless Count Per Charaster:")
print(countPerCharCaseless(strToCount))
