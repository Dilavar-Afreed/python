
#largest prime factor of a number 

num=input("enter a number")
l=[]
p=[]
for i in range(2,num):
    if num%i==0:
        l.append(i)
for j in l:
    for k in range(2,j):
        if j%k==0:
            break
    else:
        p.append(j)

print(p[-1])



   
