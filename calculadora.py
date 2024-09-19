import os
import time

while True:
    os.system('clear')
    print("\nCalculadora")
    print("============")
    print("0: Soma")
    print("1: Subtração")
    print("2: Multiplicação")
    print("3: Divisão")
    print("4: Exponenciação")
    print("5: Sair")  # Opção para sair


    try:
        opc = int(input("Escolha a operação que deseja realizar: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número entre 0 e 5.")
        time.sleep(2)  # Espera 2 segundos antes de limpar a tela novamente
        continue  # Volta para o início do loop se a entrada não for um número

    if opc == 5:
        print("Encerrando a calculadora...")
        time.sleep(2)  # Espera 2 segundos antes de encerrar o programa
        break  # Sai do loop e encerra o programa

    # Realiza a operação correspondente
    match opc:
        case 0:
            num1 = float(input("Informe o primeiro número: "))
            num2 = float(input("Informe o segundo número: "))
            soma = num1 + num2
            print(f"O valor da soma é {soma}")
        case 1:
            num1 = float(input("Informe o primeiro número: "))
            num2 = float(input("Informe o segundo número: "))
            sub = num1 - num2
            print(f"O valor da subtração é {sub}")
        case 2:
            num1 = float(input("Informe o primeiro número: "))
            num2 = float(input("Informe o segundo número: "))
            mult = num1 * num2
            print(f"O valor da multiplicação é {mult}")
            
        case 3:
            num1 = float(input("Informe o primeiro número: "))
            num2 = float(input("Informe o segundo número: "))
            if num2 == 0:
                print("Não é possível dividir por zero.")
            else:
                div = num1 / num2
                print(f"O valor da divisão é {div}")
               
        case 4:
            num1 = float(input("Informe o primeiro número: "))
            num2 = float(input("Informe o segundo número: "))
            exp = num1 ** num2
            print(f"O valor da exponenciação é {exp}")
        case _:
            print("Opção inválida. Tente novamente.")