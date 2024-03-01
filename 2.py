# Desenvolva um programa que seja capaz de calcular a média ponderada de um aluno. Inicialmente solicite
# o nome e as três notas do aluno, logo após, calcule e exiba na tela a média. Na média ponderada considere
# os seguintes pesos nas notas: 2.3 e 5. Essa é a fórmula para calcular a média:
# mediafinal = (((n1*2)+(n2*3)+(n3*5))/10)


nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota 1 do aluno: "))
nota2 = float(input("Digite a nota 2 do aluno: "))
nota3 = float(input("Digite a nota 3 do aluno: "))

media_final = (((nota1*2)+(nota2*3)+(nota3*5))/10)

print(f"Aluno: {nome_aluno}")
print(f"Média: {media_final}")
