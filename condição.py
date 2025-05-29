salario01 = float(input("Digite o seu salario"))
if salario01 <= 1692.72:
    inss = salario01 * 0.08

elif salario01 >= 1692.72 and salario01 <= 2822.90:
 inss = salario01 * 0.09

elif salario01 >= 2822.90 and salario01 <=5645.90:
   inss = salario01 * 0.11
   salario_liquido = salario01 - inss
   
print(f"A contribuição do INSS: R${inss:.2f}")
print(f"Salario bruto é: R${salario01:.2f}")
print(f"Salario liquido é: R${salario_liquido:.2f}")