import sys
n = int(input())

list=[]
dict ={}

for _ in range(n):
    list.append(sys.stdin.readline().strip())

for l in list :
    if l in dict:
        dict[l]+=1
    else:
        dict[l]=1
dict= sorted(dict.items())

max_num=0
max_book=""

for book in dict:
    if max_num<book[1]:
        max_num =book[1]
        max_book=book[0]


print(max_book)
## 막힌 부분 가장 많이 팔린 책이 여러개일 경우 사전 순으로 가장 앞서는 제목을 출력할 것
