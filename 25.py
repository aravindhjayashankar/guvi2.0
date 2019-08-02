s=int(input())
x = list(map(int, input().split()))
x.sort()
n=len(x)
if(n%2!=0):
    z=(n)//2
    print(x[z])
else:
    ans=x[n//2]+x[(n-1)//2]
    j=ans/2
    print(j)

