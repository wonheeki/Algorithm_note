## 첫번째  n을 입력받아 int로 바꾸어 count 변수에 저장한다
count =int(input())
list_of_list=[]
for _ in range(count-1):
    # 입력을 받는다
    parsed_list = map(int,input().split(" "))
    list_of_list.append(parsed_list)
print(list_of_list)