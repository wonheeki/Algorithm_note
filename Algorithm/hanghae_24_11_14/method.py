# input : 입력함수
# print : 출력함수
input_var = input('정수를 입력해주세요')
print(input_var)

# end : 개행문자
# sep : 구분자
print("a","b","c" ,end="/" , sep=".")
print("d")


# len() : 객체나 문자열의 길이
v1 = "hello"
v2 = [1, 2, 3]

len(v1), len(v2)


# map() : 개별 기능 적용
v1 = [1, 5, 10]
print("적용 전 >>",v1)
v2 = list(map(str, v1))
print("적용 후 >>",v2)


v1 = [1, 4, 10]
# min() : 최솟값
min(v1) # 1

# max() : 최댓값
max(v1) # 10

# sum() : 합계
sum(v1) # 15


# zip() : 두 그룹의 데이터를 엮어줌

list1 = [0, 1, 2, 3, 4]
list2 = ['A', 'B', 'C', 'D']
print(list(zip(list1, list2)))
# [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')]


# sorted() : 정렬
list3 = [10, 2, 7, 4, 5, 20, 58]
print("sorted 함수 >> ",sorted(list3))
# [2, 4, 5, 7, 10, 20, 58]


# reversed : interable 타입의 담긴 원소들을 역순으로 순회
list4 = [10, 2, 7, 4, 5, 20, 58]
print("reversed 함수 >> ",list(reversed(list4)))
# [58, 20, 5, 4, 7, 2, 10]

for x in reversed(list4):
    print(x)