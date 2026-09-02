texto = input("Introduza um texto: ")

palavras = texto.split()

ocorrencias = {}

for palavra in palavras:
    if palavra in ocorrencias:
        ocorrencias[palavra] += 1
    else:
        ocorrencias[palavra] = 1

for palavra in sorted(ocorrencias):
    print(palavra, ":", ocorrencias[palavra])