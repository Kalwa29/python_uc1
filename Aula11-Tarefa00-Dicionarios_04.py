pessoa_1={"nome" : "Saulo", "notas" :[5, 8, 10, 10]}
pessoa_2={"nome" : "Josué", "notas" :[6, 8.50, 9, 10]}
pessoa_3={"nome" : "Gabriel", "notas" :[7, 8, 9.50, 10]}

print(f"Dados do aluno 1{pessoa_1}")

print(f'As notas do aluno {pessoa_1["nome"]} são {pessoa_1["notas"]}')

print(f"Dados do aluno 1{pessoa_2}")

print(f'As notas do aluno {pessoa_2["nome"]} são {pessoa_2["notas"]}')

print(f"Dados do aluno 1{pessoa_3}")

print(f'As notas do aluno {pessoa_3["nome"]} são {pessoa_3["notas"]}')

media = sum("notas") / len("notas")