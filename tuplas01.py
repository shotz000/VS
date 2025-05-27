cores = ('preto','branco','verde','vermelho')
print("Minha tuplas de cores é",cores)

#Acessando elemetos de tuplas pelo indice
print("Primeira cor:",cores[0])
print("Segunda cor:",cores[1])
print("Terceira cor:",cores[2])
print("Quarta cor:",cores[3])

#Tentando modificar um elemento da tupla (isso gerará um erro)
#Cores[1] = "vermelho" #Descomente esta linha para ver o erro

#Descobrindo o tamanho da tuplas
print("Numero de cores na tuplas",len(cores))

#Percorrendo a tupla com um loop
print("Listando todas as cores na tupla:")
for cor in cores:
    print(cor)

#Verificando se um elemento esta na tupla
if "branco" in cor:
    print("branco está na tupla!")

#Criando um tupla de um unico elemento (nota a virgula no final)
unica_cores = ("preto",)
print("Tupla de um unico elemnto:",unica_cores)