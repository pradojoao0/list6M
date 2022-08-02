vet = [int(i) for i in input().split(" ") if i]

k = 17

xbreak = False

for i in range(0, len(vet)):
    if(xbreak == False):
        for j in range(0, len(vet)):
            if(vet[i] + vet[j] == k):
                print(f"({i},{j})")
                xbreak = True
                break
    else:
        break


if(xbreak == False):
    print("(n,n)")
