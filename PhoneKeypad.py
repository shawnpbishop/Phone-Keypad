#This program is written by Shawn Bishop.

def getNumber(s):
    for ch in s:
        if ch.isalpha():
            
            if ord(ch)>=65 and ord(ch)<= 67:
                print(2, end='')
            elif ord(ch)>=68 and ord(ch)<= 70:
                print(3, end='')
            elif ord(ch)>=71 and ord(ch)<= 73:
                print(4, end='')
            elif ord(ch)>=74 and ord(ch)<= 76:
                print(5, end='')
            elif ord(ch)>=77 and ord(ch)<= 79:
                print(6, end='')
            elif ord(ch)>=80 and ord(ch)<= 83:
                print(7, end='')
            elif ord(ch)>=84 and ord(ch)<= 86:
                print(8, end='')
            elif ord(ch)>=87 and ord(ch)<= 90:
                print(9, end='')
            elif ord(ch)>=97 and ord(ch)<= 99:
                print(2, end='')
            elif ord(ch)>=100 and ord(ch)<= 102:
                print(3, end='')
            elif ord(ch)>=103 and ord(ch)<= 105:
                print(4, end='')
            elif ord(ch)>=106 and ord(ch)<= 108:
                print(5, end='')
            elif ord(ch)>=109 and ord(ch)<= 111:
                print(6, end='')
            elif ord(ch)>=112 and ord(ch)<= 115:
                print(7, end='')
            elif ord(ch)>=116 and ord(ch)<= 118:
                print(8, end='')
            elif ord(ch)>=119 and ord(ch)<= 122:
                print(9, end='')
        else:
            print(ch, end='')
    
def main():
    s=input("Enter a string: ").strip()
    getNumber(s)

main()
    
