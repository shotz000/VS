print("PIZZARIA OF THE KING - WELCOME")
print("_____CARDAPIO - PREÇOS_____")
print(" ")
print("******* PIZZAS - SABORES ******")
print("CALABREZA,FRANGO,CATUPIRY")
print("*******  PIZZAS - TAMANHO  *******")
print("  PIZZA PEQUENA  R$ 10,00")
print("  PIZZA MEDIA    R$ 15,00")
print("  PIZZA GRANDE   R$ 20,00")
print("******  REFRIGERANTES  ******")
print("  COCA-COLA      R$ 7,00  ")
print("  GUARANÁ        R$ 6,00  ")
print("  FANTA          R$ 5,00  ")
print("________________________________")
print(" ")


print("DIGITE O TAMANHO DA PIZZA")
print("P - PEQUENA")
print("M - MÉDIA")
print("G - GRANDE")
print("_________")

#Lê a escolha do tamanho da pizza do usuário e converta para valor inteiro.
tampizza = input().upper()


print("FAÇA SEU PEDIDO DE SABOR DE PIZZA:")
print("1 - CALABRESA")
print("2 - FRANGO")
print("3 - CATUPIRY")
print("_________")


#Lê a escolha do sabor da pizza do usuário e converta para maiúsculo.
pedidopizza = input().upper()


print("FAÇA SEU PEDIDO PARA REFRIGERANTE:")
print("1 - COCA-COLA")
print("2 - GUARANÁ")
print("3 - FANTA")
print("_________")


#Lê a escolha do refrigerante do usuário e converta para maiúsculo.
pedidorefri = int(input())



#Calcular preços
if(pedidopizza == "1") and (tampizza == "P") and (pedidorefri==1):
   var = 10+7
   pedidos="Calabresa, Pequena, Coca-Cola"

elif(pedidopizza == "1") and (tampizza == "P") and (pedidorefri==2):
   var = 10+6
   pedidos= "Calabresa, Pequena, Guaraná"

elif(pedidopizza == "1") and (tampizza == "P") and (pedidorefri==3):
   var  = 10+5
   pedidos= "Calabresa, Pequena, Fanta"

elif(pedidopizza== "2") and (tampizza== "P") and (pedidorefri==1):
  var = 10+7
  pedidos= "Frango, Pequena, Coca-Cola"

elif(pedidopizza== "2") and (tampizza== "P") and (pedidorefri==2):
  var = 10+6
  pedidos= "Frango, Pequena, Guaraná"

elif(pedidopizza== "2") and (tampizza== "P") and (pedidorefri==3):
  var = 10+5
  pedidos= "Frango, Pequena, Fanta"

elif(pedidopizza== "3") and (tampizza== "P") and (pedidorefri==1):
  var = 10+7 
  pedidos= "Catupiry, Pequena, Coca-Cola"

elif(pedidopizza== "3") and (tampizza== "P") and (pedidorefri==2):
  var = 10+6
  pedidos= "Catupiry, Pequena, Guaraná"

elif(pedidopizza== "3") and (tampizza== "P") and (pedidorefri==3):
  var = 10+5
  pedidos= "Catupiry, Pequena, Fanta"

#Todas pequenas

elif(pedidopizza== "1") and (tampizza== "M") and (pedidorefri==1):
  var = 15+7
  pedidos= "Calabresa, Média, Coca-Cola"

elif(pedidopizza== "1") and (tampizza== "M") and (pedidorefri==2):
  var = 15+6
  pedidos= "Calabresa, Média, Guaraná"

elif(pedidopizza== "1") and (tampizza=="M") and (pedidorefri==3):
  var = 15+5
  pedidos= "Calabresa, Média, Fanta"

elif(pedidopizza== "2") and (tampizza=="M") and (pedidorefri==1):
  var = 15+7
  pedidos= "Frango, Média, Coca-Cola"

elif(pedidopizza== "2") and (tampizza=="M") and (pedidorefri==2):
  var = 15+6
  pedidos= "Frango, Média, Guaraná"

elif(pedidopizza== "2") and (tampizza=="M") and (pedidorefri==3):
  var = 15+5
  pedidos= "Frango, Média, Fanta"

elif(pedidopizza== "3") and (tampizza=="M") and (pedidorefri==1):
  var = 15+7
  pedidos= "Catupiry, Média, Coca-Cola"

elif(pedidopizza== "3") and (tampizza=="M") and (pedidorefri==2):
  var = 15+6
  pedidos= "Catupiry, Média, Guaraná"

elif(pedidopizza== "3") and (tampizza=="M") and (pedidorefri==3):
  var = 15+5 
  pedidos= "Catupiry, Média, Fanta"

#Todas médias

elif(pedidopizza== "1") and (tampizza=="G") and (pedidorefri==1):
  var = 20+7
  pedidos= "Calabresa, Grande, Coca-Cola"

elif(pedidopizza== "1") and (tampizza=="G") and (pedidorefri==2):
  var = 20+6
  pedidos= "Calabresa, Grande, Guaraná"

elif(pedidopizza== "1") and (tampizza=="G") and (pedidorefri==3):
  var = 20+5 
  pedidos= "Calabresa, Grande, Fanta"

elif(pedidopizza== "2") and (tampizza=="G") and (pedidorefri==1):
  var = 20+7
  pedidos= "Frango, Grande, Coca-Cola"

elif(pedidopizza== "2") and (tampizza=="G") and (pedidorefri==2):
  var = 20+6
  pedidos= "Frango, Grande, Guaraná"

elif(pedidopizza== "2") and (tampizza=="G") and (pedidorefri==3):
  var = 20+5
  pedidos= "Frango, Grande, Fanta"

elif(pedidopizza== "3") and (tampizza=="G") and (pedidorefri==1):
  var = 20+7
  pedidos= "Catupiry, Grande, Coca-Cola"

elif(pedidopizza== "3") and (tampizza=="G") and (pedidorefri==2):
  var = 20+6
  pedidos= "Catupiry, Grande, Guaraná"

elif(pedidopizza== "3") and (tampizza=="G") and (pedidorefri==3):
  var = 20+5
  pedidos= "Catupiry, Grande, Fanta" 

#Todas Grandes

else:
  var=0
  pedidos="Opções Inválidas"

#Pedido errado


print("////////////////////////////////////")
print(f"O TOTAL A PAGAR É: R$ {var}")
print("////////////////////////////////////")
print(f"OS PEDIDOS FORAM {pedidos}")
print("////////////////////////////////////")
print("BOM APETITE,AGRADECEMOS A PREFERENCIA !!!")