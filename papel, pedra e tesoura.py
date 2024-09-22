import random
import logging

# Configuração do logging
logging.basicConfig(filename="jogo.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

placar_jogador = 0
placar_computador = 0
computador = ["pedra", "papel", "tesoura"]

while True:
    print("===========================================")
    print("Bem Vindo ao jogo de Pedra, Papel e Tesoura")
    print("===========================================")

    print("Placar")
    print(f"Você: {placar_jogador}")
    print(f"Computador: {placar_computador}")

    print("Escolha seu lance:")
    print("0 - Pedra | 1 - Papel | 2 - Tesoura")
    
    try:
        escolha = int(input("Informe sua escolha: "))

        if escolha < 0 or escolha > 2:
            print("Opção Inválida! Tente novamente.")
            logging.warning(f"Jogador escolheu um número inválido: {escolha}")
            continue

        escolha_computador = random.choice(computador)
        
        if escolha == 0:
            print("Você escolheu Pedra")
        elif escolha == 1:
            print("Você escolheu Papel")
        elif escolha == 2:
            print("Você escolheu Tesoura")

        print(f"O computador escolheu: {escolha_computador}")

        if (escolha == 0 and escolha_computador == "pedra") or \
           (escolha == 1 and escolha_computador == "papel") or \
           (escolha == 2 and escolha_computador == "tesoura"):
            print("Deu empate!")
            placar_computador += 1
            placar_jogador += 1
            logging.info(f"Empate: Jogador escolheu {computador[escolha]} e Computador escolheu {escolha_computador}")
        elif (escolha == 0 and escolha_computador == "tesoura") or \
             (escolha == 1 and escolha_computador == "pedra") or \
             (escolha == 2 and escolha_computador == "papel"):
            print("Você Venceu!")
            placar_jogador += 1
            logging.info(f"Jogador venceu: Jogador escolheu {computador[escolha]} e Computador escolheu {escolha_computador}")
        else:
            print("O computador venceu!")
            placar_computador += 1
            logging.info(f"Computador venceu: Jogador escolheu {computador[escolha]} e Computador escolheu {escolha_computador}")

        while True:  # Loop para validar a entrada
            print("Quer jogar novamente? (s/n)")
            nova_jogada = input().lower()
            if nova_jogada == 's':
                break  # Sai do loop para jogar novamente
            elif nova_jogada == 'n':
                print("Obrigado por jogar")
                exit()  # Encerra o programa
            else:
                print("Entrada inválida! Por favor, insira 's' ou 'n'.")
    except ValueError:
        print("Entrada inválida! Por favor, insira um número (0, 1 ou 2).")
        logging.error("Entrada inválida, não é um número inteiro.")