n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

def ordem_atendimento(pacientes):
    def prioridade(paciente):
        nome, idade, status = paciente
        if status == "urgente":
            return (0, -idade)  # prioridade máxima
        elif idade >= 60:
            return (1, -idade)  # prioridade média
        else:
            return (2, 0)       # prioridade normal
        
    return sorted(pacientes, key=prioridade)

atendimentos = ordem_atendimento(pacientes)
nomes = [p[0] for p in atendimentos]
print("Ordem de Atendimento:", ", ".join(nomes))
