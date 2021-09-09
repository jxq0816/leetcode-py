a=[3,5,7,6,8,2,7,3]
for i in range(0,len(a)):
    flag=False
    for j in range(i,len(a))[::-1]:
        if a[j]<a[j-1]:
            t=a[j]
            a[j]=a[j-1]
            a[j-1]=t
            flag=True
    if flag==False:
        break

for i in range(0,3):
    print(a[i])