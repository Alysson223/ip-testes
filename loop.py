# Inicializar a lista para armazenar as notas
notas = []

while True:
    # Solicitar ao usuário para inserir uma nota
    nota = float(input("Digite a nota do aluno (digite -1 para encerrar): "))

    # Verificar se o usuário digitou -1 para encerrar
    if nota == -1:
        break

    # Adicionar a nota à lista de notas
    notas.append(nota)

# Exibir as notas inseridas
print("Notas inseridas:", notas)
