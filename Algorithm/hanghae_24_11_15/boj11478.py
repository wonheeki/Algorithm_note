# 총 문자열의 길이를 알아야하고
# 중복되는 단어가 없어야 하고
# 슬라이싱을 사용해서 자릿수별로 단어 나눠주기
# ex) str = asdf
#       a [0] s [1] d [2] f[3]
#       as [0:2] sd [1:3] df [2:4]
#       asd [0:3] sdf[1:4]
#       asdf [0:4]


str = input()
str_set=set()

for i in range(len(str)):
    for j in range(i,len(str)):
        str_set.add(str[i:j+1])
    # else:
    #     str_list.append(str[0:i+1])
# print(str_list)
# print(len(str))
print(len(str_set))

