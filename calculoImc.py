import time

# Solicitar a altura e o peso do usuário
print("Bem Vindo a Calculadora de IMC.")
print("Informe sua altura (em metros):")
altura = input();
altura = float(altura)

print("Informe seu peso (em kg):")
peso = input();
peso = float(peso)

print("Calculando ...");
time.sleep(1)
# Calcular o IMC: Peso (kg) ÷ (Altura (m) × Altura (m))
imc = peso / (altura ** 2)

# Exibir o IMC
print("================")
print(f"Seu IMC é: {imc:.2f}")  # Usar f-string para exibir o valor com 2 casas decimais

        