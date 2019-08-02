s=int(input())
ls=list(map(int,input().split()[:s]))
for i in range(s):
  print(ls[i],i)
