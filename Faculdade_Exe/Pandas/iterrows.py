# Crie um dicionário a partir do dataframe das matérias. A chave do dicionário deverá ser o código da matéria e o valor deverá ser o nome da matéria

import random

nomes = [
    "Joao", "Sara", "Pedro", "Ester", "Camila", "Maurício", "Carla", "Joana", "Maria", "Natália", "Luiz", "Marcos"
]
materias = {
    1: "Biologia", 2: "Física", 3: "Matemática",
    4: "Geografia", 5: "Português", 6: "Inglês"
}

with open("materias.csv", "w") as outp:
    outp.write(f"codigo_disciplina, nome_disciplina\n")
for chave, valor in materias.items():
    outp.write(f"{chave}, {valor}\n")
