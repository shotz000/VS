#Define uma função chamada retorna_soma
#que receba dois parametros (A e B)
def retorna_soma (a,b):
    #Retorna a soma dois parametros
    return a + b

#Inicio do programa principal
#Solicita ao usuario que digite dois valores inteiros
print("Digite dois valores:")


#Lê o segundo valor e converte para inteiro
valor1 = int(input())
#Le o segundo valor e converte para inteiro
valor2 = int(input())


#Chama a função retorna_soma passando os valores digitados
#como argumentos
resultado = retorna_soma(valor1,valor2)

#Exiba o resultado da soma
print("O resultado da soma é:",resultado)