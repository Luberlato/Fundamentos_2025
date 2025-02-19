horas = int(input("Quantas horas você trabalha:"))
dias = int(input("Quantos dias voce trabalha por mês"))
valor_hora = int(input("Quanto vale a sua hora de trabalho"))
salario_bruto = horas*valor_hora*dias
ir = salario_bruto*0.11
inss = salario_bruto*0.08
sindicato = salario_bruto*0.05
salario_liquido = salario_bruto - ir - inss - sindicato
print(f"salario bruto: R${salario_bruto:.2f}")
print(f"Desconto INSS: R${inss:.2f}")
print(f"Desconto Imposto de Renda: R${ir:.2f}")
print(f"Desconto Sindicato: R${sindicato:.2f}")
print(f"Salario Liquido: R${salario_liquido:.2f}")
