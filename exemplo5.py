valor = float(input("Insira o valor :"))
taxa = float(input("Insira a porcentagem da taxa :"))
tempo = int(input("Insira o tempo em dias :"))

prestacao = valor + (valor * taxa / 100 * tempo)

print(f"Esse é o valor da prestação: {prestacao}")