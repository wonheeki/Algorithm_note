n, k =map(int, input().split())

arr1=[]
arr2=[]
for i in range(1,n+1):
    if n%i==0:
        arr1.append(i)

for i in range(1,k+1):
    if k%i==0:
        arr2.append(i)

print(arr1,arr2)