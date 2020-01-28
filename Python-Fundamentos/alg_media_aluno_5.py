"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média do aluno
"""
#Entrando com os dados do aluno
n1 = float(input("Informe sua primeira nota: "))
n2 = float(input("Informe sua segunda nota: "))
n3 = float(input("Informe sua terceira nota: "))
n4 = float(input("Informe sua quarta nota: "))

#Calculando a média do aluno
media = float(n1 + n2 + n3 + n4)/4

#Na saída dos dados eu limitei as casas decimais
print("A média final do aluno foi: %.2f" % (media))
