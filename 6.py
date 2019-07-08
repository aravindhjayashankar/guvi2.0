year=int(input(""))
if year%4==0 or year%400==0:
    if year%100==0:
        print("not an leap year")
    else:
        print("leap year")
else:
    print("no")
