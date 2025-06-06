import notas
n1 = float(input('Digite a nota do 1 trabalho:'))
n2 = float(input('Digite a nota de Avaliação Formativa:'))
n3 = float(input('Digite a nota do 2 trabaljo:'))
n4 = float(input('Digite a nota de Avaliaçãom Integrada:'))
print('')
media_final = notas.media_aluno(n1,n2,n3,n4)
print('A media final do aluno é:',media_final)
if media_final < 6:
    situacao_final = 'Recuperaação'
else:
    situacao_final = 'Aprovado'
print('A situação final do aluno é:',situacao_final)