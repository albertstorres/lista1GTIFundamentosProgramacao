# Uma revendedora de carros paga a seus funcionários vendedores um salário fixo por mês, mais uma comissão 
# também fixa para cada carro vendido de mais 5% do valor das vendas por ele efetuadas. EScrever um algoritmo
# que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e o valor que 
# ele recebe por carro vendido. Calcule e escreva o salário fixo e o valor que ele recebe por carro vendido.
# Calcule e escreva o salário final do vendedor.

numero_carros_vendidos = int(input("Diogite o número de carros vendidos: "))
valor_total_vendas = float(input("Digite o total das vendas: "))
salario_fixo = float(input("Digite o salário fixo: "))
valor_por_carro_vendido = float(input("Digite o valor recebido por carro vendido: "))

salário_final = (((valor_total_vendas * 0.05) + (valor_por_carro_vendido * numero_carros_vendidos)) + salario_fixo)

print (f"O salário final do vendedor: R$ {salário_final}")