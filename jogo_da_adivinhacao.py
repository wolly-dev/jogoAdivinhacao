#Importando uma biblioteca
import random

#Gera um número aleatório
numero_secreto = random.randint(1, 100)
print("Bem vindo ao jogo da adivinhação!")
print("Tente adivinhar o número entre 1 e 100")

#Será requisitado ao usuário um palpite
#palpite = int(input("Digite o seu palpite: "))


#while palpite != numero_secreto:
#    if palpite < numero_secreto:
#        print("Erou! Chuta mais alto")
#        palpite = int(input("Digite o seu palpite: "))
#    elif palpite > numero_secreto:
#        print("Erou! Chuta mais baixo.")
#        palpite = int(input("Digite o seu palpite: "))
#    else:
#        print("Boa, você acertou!")

palpite = ''

while palpite != numero_secreto:
    palpite = int(input("Digite o seu palpite: "))
    if palpite == numero_secreto:
        print("Isso aí! Você acertou.")
    elif palpite < numero_secreto:
        print("Erou! Chuta mais alto.")
    else:
        print("Erou! Chuta mais baixo.")
    