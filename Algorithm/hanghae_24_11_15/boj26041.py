phone_list = input().split()
phone_num = input()
cnt=0

for i in range(len(phone_list)):
    # print(phone_list[i][0:len(phone_num)])
    if phone_list[i][0:len(phone_num)] == phone_num and phone_list[i] != phone_num:
        cnt+=1
print(cnt)