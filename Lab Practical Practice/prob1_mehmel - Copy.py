'''
   Program: prob1_mehmel.py
   Author: Lucas Mehmel
   Room:
'''
def isNumber(s):
	for ch in s:
		if not (ch >= '0' and ch <='9'):
			return False
	return True

def squishBlanks(s):
	while "  " in s:
		s = s.replace("  ", " ")
	return s
'''
x = "573"
print(isNumber(x))
x = "cat47"
print(isNumber(x))

x = "The best years            of           our  lives!"
x = squishBlanks(x)
print(x)
'''
longestWord = ""
line = input("Type a line: ")

while line != "QUIT":
        line = line.replace("?", " ")
        line = line.replace(",", " ")
        line = line.replace(".", " ")
        line = line.replace("!", " ")
        line = squishBlanks(line)
        
        line = line.split(" ")
        
        
        for word in line:
                if (len(word) > len(longestWord)) and not isNumber(word):
                        longestWord = word
        line = input("Type a line: ")    

print("Longest word = ", longestWord, len(longestWord)) 

    
    
