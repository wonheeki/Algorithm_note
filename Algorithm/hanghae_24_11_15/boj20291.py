# import sys
#
# n = int(input())
# file_list=[]
#
# for _ in range(n):
#     file_name = sys.stdin.readline().split(".")[-1].strip()
#     file_list.append(file_name)
#
# dedupe_file_list= sorted(set(file_list))
#
#
# for d in dedupe_file_list:
#     for f in file_list:
#         if d == f:
#             cnt += 1
#             file_list.remove(f)


    # print(d,cnt)

## 첫번째 시도 : 결과는 나오지만 시간초과


## 해결법 : 입력을 sys module을 사용하고
## 확장자가 카운팅 되면 리스트에서 해당 문자를 pop 하도록

## 두번째 시도 : 딕셔너리 사용
## 딕셔너리에 확장자가 없다면 확장자 키를 추가하고 1 넣어주기
## 값이 있다면 +1


import sys

n = int(input())
file_list=[]
file_dict={}

for _ in range(n):
    file_name = sys.stdin.readline().split(".")[-1].strip()
    file_list.append(file_name)

for file in file_list:
    if file_dict.get(file):
        file_dict[file]+=1
    else:
        file_dict[file]=1

file_dict = sorted(file_dict.items())
# 그냥 sorted(file_dict)하니까 value가 안보임

for e,num in file_dict:
    print(e,num)