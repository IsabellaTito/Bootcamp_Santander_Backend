# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:

for _ in range(n):
    entrada = input().strip() 
    
    nome, tema = entrada.split(",")
    tema = tema.strip()
    nome = nome.strip()

    if tema not in eventos.keys():
        eventos[tema] = [nome]
    else:
        eventos[tema].append(nome)

# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")