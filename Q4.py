vet = [int(i) for i in input().split(" ") if i]


soma = True

for i in range(0, len(vet)):
    if(i != (len(vet)/2) - 1):
        if(vet[i] + vet[len(vet) - 1 - i] > vet[i + 1] + vet[len(vet) - 2 - i]):
            continue
        else:
            soma = False
            break
    else:
        break

if(soma == True):
    print("E sim de soma convergent")
else:
    print("NAO e de soma convergente")
