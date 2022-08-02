vetY = [2.5, 2.8, 4.2, 1.4, 1.6, 4.4, 1.4, 2.5, 0.1, 0.2, 3.7, 1.7, 1.4, 1.0, 1.1, 2.3, 1.4, 3.5, 4.8, 2.3]

vetX = [float(i) for i in input().split(" ") if i]


soma = 0
for i in range(0, len(vetX)):
    soma += (1/(9*(i + 1)))*vetX[i]*vetY[20 - 1 - i]
print("{:.2f}".format(soma))
