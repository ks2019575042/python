n = int(input("정수:"))
if n>=0:
    sum=n
else:
    sum=0
while n!=0:
    n = int(input("정수:"))
    if n>0:
        sum+=n
print("합:",sum)
