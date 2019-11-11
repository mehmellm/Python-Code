import sys
import myStack
def main():
    while True:
        ab = make_empty_stack()
        ac = make_empty_stack()
        s = str(input("Enter input string"))
        if s == "quit":
            sys.exit()
        elif len(s)==0:
            print("String is in language L")
            break
        for i in range(0,len(s)+1):
                if s[i] == "a":
                    push(ab, "a")
                    push(ac, "a")
                elif s[i] == "b":
                    pop(ab)
                elif s[i] == "c":
                    pop(ac)
                else:
                    print("input must only contain a's b's and c's")
                    break
        if is_empty(ab)== None:
            print(s, " is in the language L!!")
            break
        elif is_empty(ac) == None:
            print(s, " is in the language L!!")
            break
        else:
            print(s, " is not in the language L")
            break
main()
                    
        
