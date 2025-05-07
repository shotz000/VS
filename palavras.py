import random

entrada = input("DIGITE AS PALAVRAS SEPARAS POR ESPAÇOS:")

if entrada:

    palavra_aleatoria = random.choice(entrada)
    print (f"A PALAVRA ALEATORIA É:{palavra_aleatoria}")

else:

    print("NENHUMA PALAVRA FOI DIGITADA")