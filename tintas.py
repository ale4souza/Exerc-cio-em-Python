print("Bem vindo a loja de tintas");


m2 = float(input("Informe a área em m2: "))

# Dados das latas e cobertura
litros_por_lata = 18
cobertura_por_litro = 3  # cada litro cobre 3 m²

litros_necessarios = m2 / cobertura_por_litro

quantidade_latas = int(litros_necessarios/18)

preco = quantidade_latas * 80;


print(f"Você precisará de {quantidade_latas} litros de tinta e custará {preco}");


