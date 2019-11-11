'''
    Program: prob2_mehmel.py
'''

def isAlpha(ch):
        if ch in "ABECDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            return True
        return False
def isVowel(ch):
        if ch in "AEIOUaeiou":
            return True
        else:
            return False

def removeVowels(string):
    '''
       The function takes in a string, which represents a sentence or phrase or title,
       The function removes all vowels except the those that starts a word.
    '''

    assert type(string) is str, "Parameter must be a string."
    newl = ""
    newl = string[0]
    for i in range(1, len(string)):
        ch = string[i]
        if not isAlpha(ch):
            newl += ch
        else:
            if string[i - 1] == " ":
                newl += ch
            else:
                if not isVowel(ch):
                    newl += ch
    return newl

line = input("Enter a line: ")
print(removeVowels(line))
                      
            
                    
                       
                   
                   
    
