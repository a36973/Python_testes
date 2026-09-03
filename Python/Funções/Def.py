def analisar_frascos(frascos):

    adequados = []
    baixos = []

    for quantidade in frascos:

        if quantidade >= 10:
            adequados.append(quantidade)
        else:
            baixos.append(quantidade)

    return adequados, baixos


frascos = [12, 5, 18, 7, 22, 9, 15]

adequados, baixos = analisar_frascos(frascos)

print("Adequados:", adequados)
print("Produção baixa:", baixos)