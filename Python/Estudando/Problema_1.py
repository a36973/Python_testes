plantas = [12, 15, 8, 20, 17]

total = 0

for quantidade in plantas:
    total = total + quantidade

print(total)

def calcular_media(plantas):
    return sum(plantas) / len(plantas)

resultado = calcular_media(plantas)

print("A média de  é:", resultado)

if resultado>=10:
    print("produção adequada")
else:
    print("produção baixa")
