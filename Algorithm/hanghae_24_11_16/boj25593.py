# 4           1 2 3 4 5    6    7

# 08:00~12:00 - - - - - pangyo puang
# 12:00~18:00 - - - - - sally boss
# 18:00~22:00 - - - - - leonard brown
# 22:00~08:00 - - - - - edward edward

# 08:00~12:00 puang pangyo choco leonard cony leonard choco
# 12:00~18:00 cony edward cony leonard moon puang edward
# 18:00~22:00 choco boss puang brown brown pangyo cony
# 22:00~08:00 choco edward puang cony moon choco boss
#
# 08:00~12:00 brown moon moon sally pangyo puang choco
# 12:00~18:00 pangyo edward boss sally moon cony pangyo
# 18:00~22:00 brown puang james moon cony choco choco
# 22:00~08:00 sally brown sally puang james moon sally
#
# 08:00~12:00 leonard pangyo - - - - -
# 12:00~18:00 boss choco - - - - -
# 22:00~08:00 moon edward - - - - -
# 22:00~08:00 moon sally - - - - -

# 0,4,8,12줄 : 4시간
# 1,5,9,13줄 : 6시간
# 2,6,10,14줄 : 4시간
# 3,7,11,15줄 : 10시간
n = int(input())
time_table = []
employee_name ={}

for i in range(n*4):
    temp_list = list(map(str,input().split()))
    # 첫번째줄과 세번째 줄은 각각 08:00~12:00, 18:00~22:00에 해당됨(근무시간 : 4시간)
    for li in temp_list:
        if li =="-":
            continue

        # 처음 입력된 이름이면 0으로 초기화
        if li not in employee_name:
            # if employee_name.get(li)
            employee_name[li] = 0


        if i %4==0 or i %4==2:
            employee_name[li]+=4
        # 두번째줄은 12:00~18:00에 해당됨(근무시간 : 6시간)
        if i %4==1:
            employee_name[li]+=6
        # 네번째줄은 22:00~08:00에 해당됨(근무시간 : 10시간)
        if i %4==3:
            employee_name[li] += 10

# if max(employee_name.values())-min(employee_name.values())<=12:
#     print("Yes")
# else:
#     print("No")
# 모든 근무 시간이 동일한지 확인
if employee_name:
    max_hours = max(employee_name.values())
    min_hours = min(employee_name.values())
    if max_hours - min_hours <= 12:
        print("Yes")
    else:
        print("No")
else:
    print("Yes")  # 아무도 근무하지 않는 경우