## STEP 1. 두 수 공백 한 칸으로 나누어 입력받기

a ,b = input().split()
a = int(a)
b = int(b)

if(a>b):
    print(">")
elif(a<b):
    print("<")
else:
    print("==")