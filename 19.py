fs=int(input(""))
fact = 1
if fs < 0:
   print("")
elif fs == 0:
   print("1")
else:
   for i in range(1,fs + 1):
       fact = fact*i
   print(fact)
