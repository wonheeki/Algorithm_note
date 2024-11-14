## 첫번째 시도

a = input()
sum = 0
list = a.split(" ")

for i in a:
    sum += i**2

print(sum%10)

## TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
## a에 들어있는 값이 str 타입이라서 계산이 안되는 걸로 추정



## 두번째 시도

list = map(int,input().split(" "))
sum = 0
for i in list:
    sum += i*i

print(sum%10)

