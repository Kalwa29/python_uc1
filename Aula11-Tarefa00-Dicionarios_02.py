#união_de_dicionarios
d1 = {"a": 1, "b": 2}
d3 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print (f"dicionarios originais:")
print (f"d1     >:{d1}")
print (f"d2     >:{d2}")
d1.update(d2)
d2.update(d3)

print(f"Dicionarios Atualizados:")
print (f"d1     >:{d1}")
print (f"d2     >:{d2}")