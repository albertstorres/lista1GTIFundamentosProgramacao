# Desenvolva um programa que leia a largura de uma parede, calcule e mostre a área a ser pintada e a 
# quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2m^2

altura = float(input("Digite a altura da parede: "))
largura = float(input("Digite a largura da parede: "))

area_parede = altura * largura
quantidade_tinta = area_parede / 2

print(f"Para pintar uma parede de {area_parede} m², você precisa de {quantidade_tinta} L de tinta")