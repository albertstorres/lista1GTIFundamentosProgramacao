# Uma fábrica de camisetas produz os tamanhos: pequeno, médio e grande. Cada uma está sendo 
# vendida por 10, 12 e 15 reais, respectivamente. Construa um algoritmo em que o usuário 
# forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda, e a máquina
# informe quanto será o valor arrecadado.

preco_p = 10
preco_m = 12
preco_g = 15

total_p = int(input("Digite o total de camisas tamanho Pequenas vendidas: "))
total_m = int(input("Digite o total de camisas tamanho Médio vendidas"))
total_g = int(input("Digite o total de camisas do tamanho Grande vendidas: "))

valor_final = (preco_g * total_g) + (preco_m * total_m) + (preco_p * total_p)

print(f"O valor arrecadado foi: R$ {valor_final}")