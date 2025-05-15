#inicializa uma lista de listas chamada MATRIZ para representar a matriz 4x4
#Cada lista interna representa uma linha da matriz,Inicializada com 4 zeros

MATRIZ = [[0] * 4 for _ in range(4)]


#Preenche a lista de indice 0 da matriz:

#Atribui o valor 0 ao elemento na linha 0,coluna 0

MATRIZ[0][0] = 0
#Atribui o valor 1 ao elemento na linha 0,coluna 1
MATRIZ[0][1] = 1
#Atribui o valor 0 ao elemento na linha 0,coluna 2
MATRIZ[0][2] = 0
#Atribui o valor 1 ao elemento na linha 0,coluna 3
MATRIZ[0][3] = 1

#Atribui o valor o ao elemento na linha 1,coluna 1
MATRIZ[1][1] = 0
#Atribui o valor 1 ao elemento na linha 1,coluna 2
MATRIZ[1][2] = 1
#Atribui o valor 0 ao elemento na linha 1,coluna 3
MATRIZ[1][3] = 0


#Exibindo os valores da matriz:
#Loop externo para percorrer os indices des linhas (0 a 3)
for contador1 in range(4):

  #Loop interno para percorrer on indices das colunas (0 a 3)
  for contador2 in range(4):
#Imprime o elemento da matriz e coluna atuais,sem adicionar uma nova linha
   print(MATRIZ[contador1][contador2],end=" ")
   #Imprime uma nova linha após a impressão de todos os elementos de uma linha da matriz
   print()