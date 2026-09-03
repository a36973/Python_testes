frascos = [12, 5, 18, 7, 22, 9, 15]

baixos = []

for quantidade in frascos:

    if quantidade < 10:
        baixos.append(quantidade)

print("Frascos com produção baixa:", baixos)