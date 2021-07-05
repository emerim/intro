#1
cat1 = float(input("Informe o valor do primeiro cateto:"))
cat2 = float(input("Informe o valor do segundo cateto:"))

if cat1 <0 or cat2 <0:
    print("O valor tem que ser negativo")

else:
    print(f"A hipotenusa é {(cat1**2+cat2**2)**(1/2)}")

#2
val1 = float(input("Escolha um número: "))
val2 = float(input("Escolha outro número: "))

if val1 > val2:
    print(f"O maior valor é o {val1}")

else:
    print(f"O maior valor é o {val2}")
    
#3
valor = float(input("Insira um valor: "))

if valor > 0 and valor < 1:
    print("O valor está entre 0 e 1")

else:
    print("O valor não está no intervalo 0 < x < 1")
    
#4
letra = input("Escolha uma letra:")
letra = letra.upper()
if letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print(f"{letra} é uma vogal")
else:
    print(f"{letra} não é uma vogal")

#5
val1 = float(input("Escolha um número:"))
val2 = float(input("Escolha outro número:"))

if val1 % val2 == 0:
    print(f"{val1} é múltiplo de {val2}")

else:
    print(f"{val1} não é múltiplo de {val2}")

#6
valor = float(input("Qual o valor da compra?"))
if valor >= 6999:
    desconto = valor*0.15
    
else:
    desconto = valor*0.05

print(f"Você obteve {desconto:.2f} reais de desconto. O valor final da sua compra é de {valor-desconto:.2f} reais")

#7
num1 = float(input("Escolha um número:"))
num2 = float(input("Escolha um número diferente:"))
if num1 == num2:
    print("Eu dise para escolher um número diferente...")
else:
    if num1 > num2:
        print(f"{num1} é o maior valor")
    else:
        print(f"{num2} é o maior valor")

#7
num1 = float(input("Escolha um número:"))
num2 = float(input("Escolha um número diferente:"))
if num1 == num2:
    print("Eu dise para escolher um número diferente...")
else:
    if num1 > num2:
        print(f"{num1} é o maior valor")
    else:
        print(f"{num2} é o maior valor")
        
#8
valor = float(input("Quantos reais você deseja sacar?"))
if (valor % 5) != 0:
    print("Valor indisponível, dirija-se a outro caixa.")
    
else:
    notas50 = int(valor/50)
    valor = valor%50
    notas10 = int(valor/10)
    valor = valor%10
    notas05 = int(valor/5)
    print(f"Você receberá {notas50} nota(s) de cinquenta reais, {notas10} nota(s) de dez reais e {notas05} nota(s) de cinco reais")

#9
l1 = float(input("Diga a medida de um dos lados do triângulo:"))
l2 = float(input("Diga a medida de outro lado do triângulo:"))
l3 = float(input("Diga a medida do lado restante do triângulo:"))
if l1 <= 0 or l2 <= 0 or l3 <= 0:
    print("Você colocou uma medida nula ou negativa!")
else:
    if l2+l3 > l1 > abs(l2-l3) and l1+l3 > l2 > abs(l1-l3) and l2+l1 > l3 > abs(l2-l1):
        print("É um triângulo válido!")
        
    else:
        print("Não é um triângulo!")
        
#10
altura = int(input("Quanto você mede? (em centímetros)"))
idade = int(input("Qual a sua idade?"))
horas = float(input("Quantas horas você já voou?"))
peso = float(input("Quanto você pesa? (em quilos)"))

if altura >= 175 and 40 >= idade <= 22 and horas > 1600 and 65 <= peso >= 95:
    print("Você pode cumpre todos os critérios!")
else:
    print("Você não cumpre todos os critérios :( ")




    