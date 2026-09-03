frascos = [12, 5, 18, 7, 22, 9, 15]


adequados=0
baixos=0


for quantidade in frascos:
    if quantidade>=10:
        adequados=adequados+1
    else:
        baixos=baixos+1
        

print("Frascos adequados:", adequados)
print("Frascos com produção baixa:", baixos)