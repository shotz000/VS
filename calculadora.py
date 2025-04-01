# Calculadora simples de dois numeros!
# Solitando as operações

num1 = float (input("Digite o Primeiro numero;"))
num2 = float(input("Digite o segundo numero"))
operador = input("Digite operação(+,-,*,/)")

# Realizando as operações

if operador == '+':
    resultado = num1 + num2

elif operador == '-':
    resultado = num1 - num2

elif operador == '/':
    if num2 !=0:
        resultado = num1 / num2

elif operador == '*':
    resultado = num1 / num2
    if num2 !=0:
        resultado = num1 / num2
    else:
     resultado = "Erro divisão por zero"
     
else:
 resultado = "Operacão invalido,Tente novamente"

print("O resultado de operação é" +str(resultado))