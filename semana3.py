numero = int(input("Escolha um número positivo:"))
if numero <= 0:
    print("O valor precisa ser positivo.")
    
else:
    if numero % 2 == 0:
        print(f"{numero} é um número é par")
        
    else:
        print(f"{numero} é um número é ímpar")