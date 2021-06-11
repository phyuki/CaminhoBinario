def marcaMatriz(matriz, n):
    for i in range(0,n):
        for j in range(0,n):
             matriz[i][j] = [matriz[i][j]] + [0]
    return matriz

n = int(input())

elem2 = []
matriz = []

for i in range(n):
  elem = input().split()
  for j in range(n):
    elem2 = elem2 + [int(elem[j])]
  matriz = matriz + [elem2]
  elem2 = []

matrizAux = marcaMatriz(matriz, n)

pos = [0,0]
sucess = 0

if matrizAux[0][0][0] == 0 or matrizAux[n-1][n-1][0] == 0:
    print("NOT OK")
    
else:
    while pos != [n-1, n-1]:
        i = pos[0]
        j = pos[1]
        aux = 1
    
        if j != n-1:
            if matrizAux[i][j+1][0] == 1 and matrizAux[i][j+1][1] == 0:
                pos = [i, j+1]
                matrizAux[i][j][1] = 1
        
            elif j != 0 and i != 0: 
                if matrizAux[i][j-1][0] == 1 and matrizAux[i][j-1][1] == 0:
                    pos = [i, j-1]
                    matrizAux[i][j][1] = 1
                else:
                    aux = 0
            else:
                aux = 0
        else:
            if matrizAux[i][j-1][0] == 1 and matrizAux[i][j-1][1] == 0:
                pos = [i, j-1]
                matrizAux[i][j][1] = 1
            else:
                aux = 0
                
        j = pos[1]        
        if aux == 0 or j == n-1:
            if i != n-1:
                if matrizAux[i+1][j][0] == 1 and matrizAux[i+1][j][1] == 0:
                    pos = [i+1, j]
                    matrizAux[i][j][1] = 1
                
                elif i != 0 and j != n-1 and j != 0:
                    if matrizAux[i-1][j][0] == 1 and matrizAux[i-1][j][1] == 0:
                        pos = [i-1, j]
                        matrizAux[i][j][1] = 1
                    else:
                        print("NOT OK")
                        break
                else:
                    print("NOT OK")
                    break
            else:
                if i == n-1 and j == n-1:
                    print("OK")
                    sucess = 1
                    break
                elif matrizAux[i-1][j][0] == 1 and matrizAux[i-1][j][1] == 0:
                    pos = [i-1, j]
                    matrizAux[i][j][1] = 1
                else:
                    print("NOT OK")
                    break

if pos == [n-1, n-1] and sucess == 0:
    print("OK")
    
