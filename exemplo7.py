Salario_Mensal = float(input("Informe o valor do seu Salário Mensal: "))
valor_Perc = float(input("Qual o porcentual de reajuste? "))

reajuste = Salario_Mensal * valor_Perc / 100 + Salario_Mensal
print (f"O valor reajustado é de {reajuste}")
