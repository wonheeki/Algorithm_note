## 일단 숫자 두 개를 입력받아함

## 첫번째 시도

# a,b = int(input())
# print(a+b)

# ValueError: invalid literal for int() with base 10: '4 5'
# 공백을 포함한 두 개의 숫자를 받을 수 없는 것으로 추측

## 두번째 시도
a, b = input().split()
print(int(a)+int(b))

## 세번째 시도
## 추가 조건 : 처음부터 정수로 입력받고 싶다면?

## map() : 여러 개의 데이터를 받아서 각각의 요소에 함수를 적용한 결과를 반환하는 내장함수
## ㄴ 사용법 : map(function, iterable)
## ㄴ        function : 각 요소에 적용할 함수
## ㄴ        iterable : 함수에 적용할 데이터 집합

c , d = map(int,input().split())
print(c+d)