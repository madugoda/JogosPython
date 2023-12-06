import random

def jogar():
    print(40 * "*")
    print("Bem vindo ao jogo do número secreto")
    print(40 * "*")

    numero_secreto = random.randint(1, 10)
    tentativas = 0
    limite = 0
    pontos = 100

    while True:
        print("""
            Níveis de dificuldade
            (1) Fácil 
            (2) Médio 
            (3) Difícil
            """)

        nivel = int(input("Defina o nível: "))

        if nivel == 1:
            limite = 7
            break
        elif nivel == 2:
            limite = 5
            break
        elif nivel == 3:
            limite = 2
            break
        else:
            print("Digite um nível válido!")

    def pontuacao(numero_secreto, chute, pontos):
        if numero_secreto != chute:
            pontos_perdidos = abs((numero_secreto - chute) * 5)
            pontos -= pontos_perdidos
        return pontos

    while limite > 0:
        chute = int(input("Digite um número de 1 a 10: "))

        if chute <= 0 or chute > 10:
            print("Digite um valor entre 1 e 10")
            continue

        tentativas += 1

        if numero_secreto > chute:
            limite -= 1
            print(f"Você errou, o número é maior. Você tem {limite} tentativas")
            pontos = pontuacao(numero_secreto, chute, pontos)
        elif numero_secreto < chute:
            limite -= 1
            print(f"Você errou, o número é menor. Você tem {limite} tentativas")
            pontos = pontuacao(numero_secreto, chute, pontos)
        else:
            pontos = pontuacao(numero_secreto, chute, pontos)
            print(f"Parabéns, você acertou em {tentativas} tentativas e fez {pontuacao(numero_secreto, chute, pontos)} pontos")
            print("Fim de jogo")
            break

    if limite == 0:
        print(f"Você perdeu, o número secreto era {numero_secreto}")
        print("Fim de jogo")

if __name__ == "__main__":
    jogar()
