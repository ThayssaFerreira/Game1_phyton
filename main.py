import random


def caca_ao_numero():
    print("Bem-vindo à Caça ao Número!")
    print("Eu escolhi um número secreto. Você consegue adivinhar?")

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 7

    while tentativas < max_tentativas:
        print(f"\nTentativa {tentativas+1}/{max_tentativas}")
        palpite = int(input("Digite o seu palpite (entre 1 e 100): "))

        if palpite == numero_secreto:
            print("Parabéns! Você encontrou o número secreto!")
            return

        elif palpite < numero_secreto:
            print("Muito baixo! Tente um número maior.")

        else:
            print("Muito alto! Tente um número menor.")

        tentativas += 1

    print("\nFim de jogo! Você ficou sem tentativas.")
    print(f"O número secreto era: {numero_secreto}")
    reiniciar_jogo()

def reiniciar_jogo():
    resposta = input("Deseja reiniciar o jogo? (s/n): ")
    if resposta.lower() == "s":
        caca_ao_numero()
    else:
        print("Obrigado por jogar!")

caca_ao_numero()
