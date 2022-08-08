import numpy as np

def printmat (matriz):

    dim = np.shape(matriz)
    b=''

    for i in range(dim[0]):
        for j in range(dim[1]):
            b += str(matriz[i][j]) + '\t'
        print(b)
        b=''


def Recomendacion(Muestra, PH):
       
    l = [['N', 'P', 'K', 'Ca', 'Mg', 'S', 'Cu', 'Mn', 'Zn', 'Fe', 'Cr', 'Ni', 'Pb', 'Cd', 'B', 'Ba', 'Se', 'As'], 
        [5.2, 2.1, 4.3, 0.5, 0.6, 0.5, 0.4, 0.4, 0.3, 0.3, 0.5, 0.3, 0.2, 0.2, 0.8, 0.9, 0.15, 0.2], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    dim = np.shape(l)

    for i in range(dim[1]):
            l[2][i] = int(input('Digite el valor de la muestra de '+ l[0][i] +'\n'))
            l[3][i] = round(l[1][i] - l[2][i],2)
   
    printmat(l)
    


def run():

    
    Muestra = input('Digite la muestra a analizar: \n')
    PH = input('Digite el pH de la muestra: \n')
    
    Recomendacion(Muestra, PH)
    



if __name__ == '__main__':
    run()