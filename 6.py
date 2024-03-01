# Faça um algoritmo para ler o salário de um funcionário e aumentá-lo em 15%. Após aumento, desconte 8%
# de impostos. Imprima o salário inicial, o salário com o aumento e o salário final.

salario = float(input("Digite o salário: "))

salario_aumento = salario * 1.15
salario_final = salario_aumento * 0.92

print(f"Salário inicial: R$ {salario}")
print(f"Salário com aumento: r$ {salario_aumento}")
print(f"Salario final: R$ {salario_final}")