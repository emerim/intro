#05/07/2021
#Lista 5 - Uso do operador condicional (IF-ELSE IF)

#EXERCÍCIO 1
l1 = float(input("Diga a medida de um dos lados do triângulo:"))
l2 = float(input("Diga a medida de outro lado do triângulo:"))
l3 = float(input("Diga a medida do lado restante do triângulo:"))

#verificar se é um triângulo mesmo
if l1 <= 0 or l2 <= 0 or l3 <= 0:
    print("Você colocou uma medida nula ou negativa!")
elif l2+l3 < l1 < abs(l2-l3) and l1+l3 < l2 < abs(l1-l3) and l2+l1 < l3 < abs(l2-l1):
    print("Não é um triângulo válido!")

#classificar os tipos de triângulo
elif l1 == l2 == l3:
    print("É um triângulo equilátero!")
elif l1 == l2 or l1 == l3 or l1 == l3:
    print("É um triângulo isóceles!")
else:
    print("É um triângulo escaleno!")
    
#EXERCÍCIO 2
a1 = float(input("Diga um dos ângulos do triângulo:"))
a2 = float(input("Diga outro ângulo do triângulo:"))
a3 = float(input("Diga o terceiro ângulo do triângulo:"))
if a1+a2+a3 != 180:
    print("A soma dos ângulos internos de um triângulo tem que ser 180º!")
elif a1 < 90 and a2 < 90 and a3 < 90:
    print("É um triângulo acutângulo.")
elif a1 == 90 or a2 == 90 or a3 == 90:
    print("É um triângulo retângulo.")
else:
    print("É um triângulo obtuso.")
    
#EXERCÍCIO 3
v1 = float(input("Insira um valor:"))
v2 = float(input("Insira outro valor:"))
v3 = float(input("Insira mais um valor:"))
if v1 == v2 or v1 == v3 or v2 == v3:
    print("Os valores precisam ser diferentes entre si")
elif v1 > v2 > v3:
    print(f"O maior valor é {v1} e o menor valor é {v3}")
elif v1 > v3 > v2:
    print(f"O maior valor é {v1} e o menor valor é {v2}")
elif v2 > v1 > v3:
    print(f"O maior valor é {v2} e o menor valor é {v3}")
elif v2 > v3 > v1:
    print(f"O maior valor é {v2} e o menor valor é {v1}")
elif v3 > v1 > v2:
    print(f"O maior valor é {v3} e o menor valor é {v2}")
else:
    print(f"O maior valor é {v3} e o menor valor é {v1}")

#EXERCÍCIO 4
valor = float(input("Qual o valor da sua compra?"))
if valor < 100:
    print("Você não tem direito ao desconto ainda")
    
else:
    nivel = input("Qual é seu nível de engajamento?")
    if nivel == "seguidor":
        print(f"Você obteve 5% de desconto! O valor final é de {(valor*0.95):.2f} reais")
    elif nivel == "comentarista":
        print(f"Você obteve 8% de desconto! O valor final é de {(valor*0.92):.2f} reais")
    elif nivel == "fã":
        print(f"Você obteve 12% de desconto! O valor final é de {(valor*0.88):.2f} reais")
    else:
        print("Você acabou de inventar esse nível!!!")
        
#EXERCÍCIO 5
t = float(input("Qual a temperatura?"))
u = input("Qual a unidade de medida? Insira apenas a inicial!").upper()
if u == "C":
    print(f"A temperatura é de {t*1.8+32}°F ou {t+273}K")
elif u == "F":
    print(f"A temperatura é de {(t-32)/1.8}°C ou {(t-32)/1.8+273}K")
elif u == "K":
    print(f"A temperatura é de {t-273}K ou {(t-273)*1.8+32}°F")
else:
    print("Unidade inválida")

#EXERCÍCIO 6
p = float(input("Qual a pressão? (em kPa)"))
t = float(input("Qual a temperatura? (em °C)"))

if p == 100:
    if t < 0:
        print("Estado sólido")
    elif t == 0:
        print("Mistura sólido-líquido")
    elif 0 < t < 100:
        print("Líquido")
    elif t == 100:
        print("Mistura líquido-vapor")
    else:
        print("Gasoso")
        
elif p == 200:
    if t == 120:
        print("Mistura líquido-vapor")
    elif t>120:
        print("Gasoso")
    else:
        print("Não consta no nosso banco de dados")
elif p == 300:
    if t == 133.6:
        print("Mistura líquido-vapor")
    elif t > 133.6:
        print("Gasoso")
    else:
        print("Não consta no nosso banco de dados")
        
elif p == 400:
    if t == 143.6:
        print("Mistura líquido-vapor")
    elif t > 143.6:
        print("Gasoso")
    else:
        print("Não consta no nosso banco de dados")
        
elif p == 500:
    if t == 151.9:
        print("Mistura líquido-vapor")
    elif t > 151.9:
        print("Gasoso")
    else:
        print("Não consta no nosso banco de dados")

else:
    print("Esse valor não consta no nosso banco de dados")
    
    