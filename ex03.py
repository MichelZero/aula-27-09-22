# 1.	Desenvolva um programa em Python que recebe do usuário um número real
# e exibe em tela se este número
# é maior, menor ou igual que zero.

# entrada de dados
numero = float(input("Digite um número real: "))

# processamento de dados
if numero > 0:
    print(f"O número {numero} é maior que zero.")
elif numero < 0:
    print(f"O número {numero} é menor que zero.")
else:
    print(f"O número {numero} é igual a zero.")

# saída de dados
print("Fim do programa.")