def calcular_dias_de_vida(idade):
    #Calcula e retorna o número aproximado de dias vividos (365 dias por ano)
    return idade * 365


#Inicio do programa principal
#solicitada ao usuario que digite o seu nome 
print("Digite o seu nome:")
nome = input()

#Socilita ao usario que digite a sua idade
print("Digite a sua idade:")
idade = int(input())


#Chama a função para calcular os dias de vida e armezena o resultado na variavel 'dias'
dias = calcular_dias_de_vida(idade)

print("Ola",nome +",voce ja viveu",dias,"dias.")