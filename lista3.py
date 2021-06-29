#1 - segundo valor maior que o primeiro
num1 = float(input("Escolha um número:"))
num2 = float(input("Escolha outro número:"))
print(num1<num2)

#2 - os dois são pares
num1 = float(input("Escolha um número:"))
num2 = float(input("Escolha outro número:"))
print(num1 % 2 == 0 and num2 % 2 == 0)

#3 - entre 0 e 1
num1 = float(input("Escolha um número:"))
print(num1 > 0 and num1 < 1)

#4 - valores diferentes entre si
num1 = float(input("Escolha um número:"))
num2 = float(input("Escolha outro número:"))
num3 = float(input("Escolha mais um número:"))
print(num1 != num2 and num2 != num3 and num3 != num1)

#5 - ordem crescente
num1 = float(input("Escolha um número:"))
num2 = float(input("Escolha outro número:"))
num3 = float(input("Escolha mais um número:"))
print(num1 < num2 and num2 < num3)

#6 - é par
num1 = float(input("Escolha um número:"))
print(num1 % 2 == 0)