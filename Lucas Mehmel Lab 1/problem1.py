'''
   Author: Lucas Mehmel
   Course: CSC 112L
   Program: problem1.py
'''
mydict = {}

def install(word, line):
    if word in mydict:
        mydict[word].append(line)
    else:
        mydict[word] = [line]

def cleanpunc(word):
    newword = ""
    for ch in word:
        if ch in "abcdefghijklmnopqrstuvwxyz" or ch == " ":
            newword += ch
    return newword

while True:
    response = input("# ")
    if response[0] == "*":
        break
    if response[0] == "?":
        word = response[1:]
        if word in mydict:
            print(mydict[word])
        else:
            print("<<NOTHING FOUND>>")
    else:
        original_line = response
        response = response.lower()
        response = cleanpunc(response)
        for word in response.split(" "):
            install(word, original_line)
   
    
