nterms = int(input())
num1 = 0
num2 = 1
count = 0
if nterms <= 0:
  print(num1)
elif nterms == 1:
   print(num2)
else:
   while count < nterms:
       print(num2,end=' ')
       nth = num1 + num2
       num1 = n2
       num2 = nth
       count += 1
