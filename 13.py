x=int(input())
if x > 1:
    for p in range(2,x):
        if(x%p==0):
            print('no')
            break
    else:
            print('yes')
else:
            print('no')
