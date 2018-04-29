print('********************************')
print('Bem vindo ao jogo de adivinhaçao')
print('********************************')

numero_secreto = 43
chute = input("Digite o seu numero: ")
print("Voce digitou: ", chute)

if numero_secreto == int(chute):
    print("Voce acertou")
else:
    print("Voce errou")

print("Fim do jogo")