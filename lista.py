#lista
filmes = ['Batman',
        'Homi do ferro (la ele)',
        'Capitão Patria',
        'Yuri Alberto',
        'Zeze de Camargo',
        'Calma Calabreso']

print('------------------------------------')
#percorrendo a lista
for filme in filmes:
    print(filme.upper())

print('------------------------------------')
#percorrendo a lista como vetor
for x in range(len(filmes)):
    print(filmes[x])