import numpy as np

def printmat (matriz):

    dim = np.shape(matriz)
    b=''

    for i in range(dim[0]):
        for j in range(dim[1]):
            b += str(matriz[i][j]) + '\t'
        print(b)
        b=''

def recomendacion(Matriz, dim):

    for i in range(dim[1]):
        if i >= 0 and i <= 2:
            #print('MACRONUTRIENTES PRIMARIOS \n')
            print('\n'+str(Matriz[0][i]) + ':\nValor Optimo de cultivo: '
            + str(Matriz[1][i]) + '\npH Muestra: '+ str(Matriz[2][i])
            + '\nResultado: '+ str(Matriz[3][i]))

            if Matriz[3][i] > 0:
                print('Recomendación 1: Incrementar pH del suelo en "resultado C20"')
                print('Recomendación 2: Optimo')
            else:
                print('Recomendación 1: disminuir pH del suelo en "resultado C20"')
                print('Recomendación 2: Incrementar macronutrientes primarios en el suelo')
        elif i > 2 and i <= 5:

            #print('MACRONUTRIENTES SECUNDARIOS \n')
            print('\n'+str(Matriz[0][i]) + ':\nValor Optimo de cultivo: '
            + str(Matriz[1][i]) + '\npH Muestra: '+ str(Matriz[2][i])
            + '\nResultado: '+ str(Matriz[3][i]))

            if Matriz[3][i] > 0:
                print('Recomendación 1: Incrementar pH del suelo en "resultado C20"')
                print('Recomendación 2: Optimo')
            else:
                print('Recomendación 1: disminuir pH del suelo en "resultado C20"')
                print('Recomendación 2: Incrementar macronutrientes secundarios en el suelo')      
        elif i > 5 and i <= 9:

            #print('MICRONUTRIENTES \n')
            print('\n'+str(Matriz[0][i]) + ':\nValor Optimo de cultivo: '
            + str(Matriz[1][i]) + '\npH Muestra: '+ str(Matriz[2][i])
            + '\nResultado: '+ str(Matriz[3][i]))

            if Matriz[3][i] > 0:
                print('Recomendación 1: Incrementar pH del suelo en "resultado C20"')
                print('Recomendación 2: Optimo')
            else:
                print('Recomendación 1: disminuir pH del suelo en "resultado C20"')
                print('Recomendación 2: Incrementar micronutrientes en el suelo')
        elif i > 9 and i <= 13:

            #print('MICRONUTRIENTES \n')
            print('\n'+str(Matriz[0][i]) + ':\nValor Optimo de cultivo: '
            + str(Matriz[1][i]) + '\npH Muestra: '+ str(Matriz[2][i])
            + '\nResultado: '+ str(Matriz[3][i]))

            if Matriz[3][i] > 0:
                print('Recomendación 1: Incrementar pH del suelo en "resultado C20"')
                print('Recomendación 2: Aprobado')
            else:
                print('Recomendación 1: disminuir pH del suelo en "resultado C20"')
                print('Recomendación 2: Peligrosidad')
        elif i > 13 and i <= 17:

            #print('MICRONUTRIENTES \n')
            print('\n'+str(Matriz[0][i]) + ':\nValor Optimo de cultivo: '
            + str(Matriz[1][i]) + '\npH Muestra: '+ str(Matriz[2][i])
            + '\nResultado: '+ str(Matriz[3][i]))

            if Matriz[3][i] > 0:
                print('Recomendación 1: Incrementar pH del suelo en "resultado C20"')
                print('Recomendación 2: Optimo')
            else:
                print('Recomendación 1: disminuir pH del suelo en "resultado C20"')
                print('Recomendación 2: Peligrosidad')




def run():
       
    l = [['N', 'P', 'K', 'Ca', 'Mg', 'S', 'Cu', 'Mn', 'Zn', 'Fe', 'Cr', 'Ni', 'Pb', 'Cd', 'B', 'Ba', 'Se', 'As'], 
        [5.2, 2.1, 4.3, 0.5, 0.6, 0.5, 0.4, 0.4, 0.3, 0.3, 0.5, 0.3, 0.2, 0.2, 0.8, 0.9, 0.15, 0.2], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    dim = np.shape(l)

    for i in range(dim[1]):
            l[2][i] = float(input('Digite el valor de la muestra de '+ l[0][i] +'\n'))
            l[3][i] = round(l[1][i] - l[2][i],2)
    
    print('\nTable: \n')
    printmat(l)
    recomendacion(l,dim)
    
  

if __name__ == '__main__':
    run()