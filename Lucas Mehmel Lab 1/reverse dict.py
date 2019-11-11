ages ={"Mark": 59, "Susie": 26, "Luke": 5, "JP": 117, "Tamara": 26, "Mike": 59, "Allison": 97}


def makeRevDict(dictionary):
    newDict = {}
    for key in dictionary.keys():
        newkey = dictionary[key]
        if newkey in newDict:
            newDict[newkey] = newDict[newkey], key
        else:
            newDict[newkey] = key
    return newDict

print(makeRevDict(ages))
