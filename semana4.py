#maior(es) valor(es) entre três

n1=float(input())
n2=float(input())
n3=float(input())

if n1 == n2 == n3:
    print("valores iguais")

elif n1>= n2 and n1 >= n3:
    print(n1)
elif n2>= n1 and n2 >= n3:
    print(n2)
else:
    print(n3)
    
#menor valor entre dois
n1 = float( input() )
n2 = float( input() )

if n1 == n2:
    print("valores iguais")

elif n1 <= n2:
    print({n1})

else:
    print({n2})