#Exercício 1
cat1 = int(input("Informe o valor do primeiro cateto:"))
cat2 = int(input("Informe o valor do segundo cateto:"))
print(f"A hipotenusa é {(cat1**2+cat2**2)**(1/2)}")

#Exercício 2
base = float(input("Qual a base do triângulo?"))
altura = float(input("Qual a altura do triângulo?"))
print(f"A área do triângulo é {base*altura/2}")

#Exercício 3
b1 = float(input("Qual a medida da base superior?"))
b2 = float(input("Qual a medida da base inferior?"))
h = float(input("Qual a altura?"))
print(f"A área do trapézio é {(b1+b2)*h/2}")

#Exercício 4
x = float(input("Qual a base?"))
a = float(input("Qual o expoente?"))
print(f"A derivada é {a*x**(a-1)}")

#Exercício 5
valorMetro = float(input("Insira a medida em metros:"))
print(f"{int(valorMetro*1000)} mm")

#Exercício 6
horas = int(input("Número de horas:"))
minutos = int(input("Número de minutos:"))
segundos = int(input("Número de segundos:"))
print(f"Total em segundos: {(horas*60+minutos)*60+segundos}")

#Exercício 7
salário = float(input("Valor do salário atual:"))
aumento = float(input("Aumento percentual:"))
print(f"O salário com aumento de de {aumento}% é de R${salário+(salário*aumento/100)}")

#Exercício 8
preço = float(input("Preço do produto:"))
desconto = float(input("Desconto percentual:"))
print(f"O preço com desconto é de {preço-(desconto*preço/100)} reais")

#Exercício 9
distancia = float(input("Qual a distância (km) a percorrer?"))
velocidade = float(input("Qual a velocidade média (km/h)?"))
print(f"O tempo estimado de viagem é de {(distancia/velocidade):.1f} horas")

#Exercício 10
celsius = float(input("Qual a temperatura em graus Celsius?"))
print(f"A temperatura em Fahrenheit é de {9*celsius/5+32}")

#Exercício 11
quilometragem = float(input("Qual o número de quilômetros percorridos?"))
dias = int(input("Por quantos dias o carro foi alugado?"))
print(f"O valor a ser pago é de {quilometragem*0.15+dias*60} reais")

#Exercício 12 - Tenso
cigarros = int(input("Quantos cigarros você fuma por dia?"))
anos = int(input("Há quantos anos você fuma?"))
minutos = anos*cigarros*365*10
print(f"Você perdeu {minutos/(60*24):.1f} dias de vida")