pessoa={"nome" : "Saulo", "idade" : 16, "cidade" : "Duque de Caxias"}
print(f"Dados da pessoa: {pessoa}")

pessoa["idade"]=17
print(f"Dados atualizad: {pessoa}")

pessoa["email"]="saulokalwa@gmail.com"
print(f"Dados atualizados: {pessoa}")

pessoa["sexo"]="M"
print(f"Dados atualizado: {pessoa}")

del pessoa["nome"]
del pessoa["email"]
print(f"Dados atualizados:{pessoa}")



