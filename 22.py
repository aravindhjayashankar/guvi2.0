s=int(input())
list=list(map(int,input().split()))
re=1
len=[]
for i in list:
  re=re*i
for i in list:
  len.append(re//i)
print(*len)
