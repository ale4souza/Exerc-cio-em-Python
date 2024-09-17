print("Bem vindo(a) ao setor de pagamento");
#print("Quanto você ganha por hora? ");

valor_hora = float(input("Quanto você ganha por hora? "));
quant_hora = float(input("Quantas horas foram trabalhadas no mês? "));

salario_bruto = valor_hora * quant_hora;


calc_ir = salario_bruto * 0.11;
calc_inss = (salario_bruto-calc_ir) * 0.08;
calc_sind = (salario_bruto-calc_ir-calc_inss) * 0.05;

salario_liq = salario_bruto - (calc_inss + calc_ir + calc_sind)

print(f"Seu salário Bruto é R${salario_bruto:.2f} ");
print(f"Você pagou ao INSS R${calc_inss:.2f}");
print(f"Você pagou de IR R${calc_ir:.2f}");
print(f"Você pagou ao Sindicato R${calc_sind:.2f}");
print(f"Seu salário líquido é de R${salario_liq:.2f}");