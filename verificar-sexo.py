#Definindo a função 'verificaSexo' que receba a variavel 'sexo'
#como parametro


def verificarSexo(sexo):
    #Verificar de o sexo é "f" para feminino
    if sexo == "f":
        #Se for feminino,imprime "Feminino"
        print("Feminino")
    else:
        #Caso contrario,imprime "Masculino"
        print("Masculino")

#Solicita ao usario para digitar seu sexo (f para feminino e m para)
#masculino)
print("Digite o seu sexo:(f) para seu feminino e (m) para masculino:)")

#le a entrada do usario e armazena na variavel 'sexo'
sexo = input()
#chama a função 'verificarSexo' passando o valor de 'sexo'
verificarSexo(sexo)