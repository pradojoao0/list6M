vet = [int(i) for i in input().split(" ") if i]

def numeroMedio():
    media = (len(vet) // 2 ) + 1
    return media

semiparticionado = False
contadorImpar = 1
contadorPar = 2
tamanho = len(vet)
media = numeroMedio()

while(semiparticionado ==  False):
    if(contadorImpar < media):
        if(vet[contadorImpar] < vet[tamanho - contadorPar]):
            aux = vet[contadorImpar]
            vet[contadorImpar] = vet[tamanho - contadorPar]
            vet[tamanho - contadorPar] = aux

        contadorPar += 2
        contadorImpar += 2
    else:
        break
print(*vet)
