s = int(input())

str_list =[]
for _ in range(s):
    num , char = input().split()
    # str_list.append({int(num):list(char)})
    char = list(char)
    new_str=""
    for i in range(len(char)):
        new_str+=char[i]*int(num)
    str_list.append(new_str)

for str in str_list:
    print(str)


# repeat을 사용해볼까

# print(len(str_list))
# for i in range(len(str_list)):


    # new_str+=str[i]*int(num)
    # str = list(char)
    # new_str = ""
    # print(len(str))
    # for i in range(len(str_list[i])):
    #     # print(str[i])
    #     new_str+=str[i]*int(num)
    #     print(new_str)
# print(str_list)

##TypeError: can't multiply sequence by non-int of type 'str'