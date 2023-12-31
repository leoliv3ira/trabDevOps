import random

def jogo_da_velha():
    opcoes = ["Pedra", "Papel", "Tesoura"]

    while True:
        jogador = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()
        if jogador not in opcoes:
            print("Escolha inválida. Tente novamente.")
        else:
            computador = random.choice(opcoes)
            print(f"Computador escolheu: {computador}")
            print(f"Você escolheu: {jogador}")

            if jogador == computador:
                print("Empate!")
            elif (
                (jogador == "Pedra" and computador == "Tesoura") or
                (jogador == "Papel" and computador == "Pedra") or
                (jogador == "Tesoura" and computador == "Papel")
            ):
                print("Você venceu!")
            else:
                print("Computador venceu!")

        jogar_novamente = input("Deseja jogar novamente? (Sim/Não): ").capitalize()
        if jogar_novamente != "Sim":
            break

if __name__ == "__main__":
    jogo_da_velha()