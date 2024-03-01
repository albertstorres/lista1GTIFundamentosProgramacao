# Leia um número e indique se ele é maior, menor ou igual a zero

numero = int(input("Digite um número inteiro: "))

if (numero > 0) :
    print(f"{numero} é MAIOR que zero")
elif (numero < 0) :
    print(f"{numero} é MENOR que zero")
else :
    print(f"{numero} é IGUAL a zero")