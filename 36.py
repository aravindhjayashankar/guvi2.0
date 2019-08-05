at=input()
count=0
for i in range(len(at)):
 if(at[i].isdigit() or at[i].isalpha() or at[i]==(" ")):
  continue
 else:
  count+=1
print(count)
