print ("Olá, seja bem vindo (a) ao cálculo de notas");
nota1 = float(input("Informe a primeira nota parcial: "));
nota2 = float(input("Informe a segunda nota parcial: "));

media = (nota1 + nota2)/2;

print(f"A média é {media}")

if media == 10:
    print("Aprovado com Distinção!Parabens!")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
