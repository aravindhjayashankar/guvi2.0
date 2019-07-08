num=int(input())
xy=num
sum=0
while num>0:
  y=num%10
  sum=sum+y*y*y
  num=num//10
if xy==sum:
  print("yes")
else:
  print("no")
