# 2.	Elabore um programa em Python que tem como saída o nome do time vencedor de uma partida
# de futebol. O seu programa deve receber os nomes dos dois times da partida e o número de gols
# marcados por cada um deles. Vence a partida aquele time que marcar o maior número de gols.
# Exiba a mensagem “EMPATE”, caso a partida não tenha tido um vencedor.

# entrada de dados
time1 = input("Digite o nome do time 1: ")
time2 = input("Digite o nome do time 2: ")
gols1 = int(input("Digite o número de gols do time 1: "))
gols2 = int(input("Digite o número de gols do time 2: "))

# processamento de dados
if gols1 > gols2:
    print(f"O time {time1} venceu a partida.")
elif gols2 > gols1:
    print(f"O time {time2} venceu a partida.")
else:
    print("EMPATE")

# saída de dados
print(f"O time {time1} marcou {gols1} gols e o time {time2} marcou {gols2} gols.")
print("Fim do programa.")