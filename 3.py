# Desenvolva um programa que leia um número inteiro. Na sequência, mostre na tela verdadeiro ou falso
# se o número digitado quando a ele somado mais 7, se torna um valor par.

numero = int(input("Digite um número inteiro: "))
numero += 7

if (numero % 2 != 0) :
    print("Falso")
else :
    print("Verdadeiro")