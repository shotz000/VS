numero = input("Digite um numero inteiro para verificar se é palindromo:")
if numero == numero[::-1]:

    print(f"O numero {numero} é um palindromo")

else:
    print(f"O numero {numero} não é um palindromo")