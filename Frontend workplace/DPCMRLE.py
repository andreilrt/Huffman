import random

class CodDPCM:

    def generarMatriz(self,size):
        matriz = [[random.randrange(0,5) for i in range(size)] for j in range(size)]
        return matriz     

    def RecorrerHorizontal(self,mensaje):
        
        vector = []
        for fila in mensaje:
            for elemento in fila:
                vector.append(elemento)
        
        return vector

    def RecorrerVertical(self,mensaje):
        
        vector = []
        for columna in range(len(mensaje)):
            for fila in range(len(mensaje)):
                vector.append(mensaje[fila][columna])
        return vector

    def RecorrerZigZag(self,mensaje):
        vector=[]
        n = len(mensaje[0])
        i = 0
        j = 0
        k = 0
        isUp = True
        while k<n * n :
            if isUp:
                while i >= 0 and j<n: 
                    vector.append(mensaje[i][j])
                    k += 1
                    j += 1
                    i -= 1
                if i < 0 and j <= n - 1:
                    i = 0
                if j == n:
                    i = i + 2
                    j -= 1
            else: 
                while j >= 0 and i<n : 
                    vector.append(mensaje[i][j])
                    k += 1
                    i += 1
                    j -= 1
                if j < 0 and i <= n - 1: 
                    j = 0
                if i == n: 
                    j = j + 2
                    i -= 1

            isUp = not isUp
        return vector


    def resta(self,vector):
        new_vector = []
        new_vector.append(vector[0])
        for x in range(len(vector)):
            if x > 0:
                new_vector.append(vector[x] - vector[x-1])
        return new_vector


    def vecSinRepeticiones(self,vector):
        norep = []

        for x in range(len(vector)):
            if (x == 0) & (vector[x] == vector[x-1]):
                norep.append(vector[x])
            if vector[x] != vector[x-1]:
                norep.append(vector[x])
        return norep

    def contarRepeticiones(self, vector):
        conteo = []
        conteo.append(0)
        y = 0
        for x in range(len(vector)):
            if (vector[x] != vector[x-1]) & (x > 0):
                conteo.append(0)
                y = y+1
            conteo[y] = conteo[y]+1

        return conteo

    def pos_neg(self,vector):
        new_vector = []
        for x in range(len(vector)):
            new_vector.append(1 if (vector[x]<0) else 0)
        return new_vector

    def vec2Binario(self,vector):
        new_vector = []
        for x in range(len(vector)):
            new_vector.append(abs(vector[x]))

        Bin = []
        for x in range(len(new_vector)):
            test = bin(int(new_vector[x]))
            binario = test[2:]
            Bin.append(binario)

        return Bin

    def findMaxBits(self,vector):
        maxN = 0
        for x in range(len(vector)):
            if len(vector[x]) > maxN:
                maxN = len(vector[x])

        return maxN


    def fillBinary(self,vector,maxB):
        for x in range(len(vector)):
            while len(vector[x])<maxB:
                vector[x] = '0' + vector[x]
        return vector

    def binarioSigned(self,filled,sign):
        signed = []

        for x in range(len(filled)):
            signed.append(str(sign[x]) + filled[x])

        return signed 

    def binarioFinal(self,rep,numeros):
        binario_final = []
        for x in range(len(numeros)):
            binario_final.append(rep[x])
            binario_final.append(numeros[x]) 
        return binario_final


    def finalProcess(self,matrizLeida):
        resta = p.resta(matrizLeida)
        print(resta)
        neg_pos = p.pos_neg(resta)
        
        rep = p.contarRepeticiones(resta)
        norep = p.vecSinRepeticiones(resta)

        absBin = p.vec2Binario(norep)
        repBin = p.vec2Binario(rep)
        
        maxBit = p.findMaxBits(absBin)
        maxBitRep = p.findMaxBits(repBin)

        fillAbs = p.fillBinary(absBin,maxBit)
        fillRep = p.fillBinary(repBin,maxBitRep)

        binarioSigned = p.binarioSigned(fillAbs,neg_pos)
        binario = p.binarioFinal(repBin,binarioSigned)
        return binario

    def contacto(self,tamaño,op,generar,matriz=[]):
        if generar:
            matriz = p.generarMatriz(tamaño)

        print('¿Como quiere que se lea la matriz?'+
        '\n1. Horizontal\n2.Vertical\n3.ZigZag\n'+
        '4.Determinar mejor opcion\n-->')

        if op == 1:
            matrizLeida = p.RecorrerHorizontal(matriz)
        elif op == 2:
            matrizLeida = p.RecorrerVertical(matriz)
        elif op == 3:
            matrizLeida = p.RecorrerZigZag(matriz)
        else:
            a = p.RecorrerZigZag(matriz)#Cambiar por ZigZag
            aa = p.finalProcess(a)
            b = p.RecorrerVertical(matriz)
            bb = p.finalProcess(b)
            c = p.RecorrerHorizontal(matriz)
            cc  = p.finalProcess(c)

            if (len(aa) < len(bb)) & (len(aa) < len(cc)):
                print('La mejor lectura es ZigZag')

                matrizLeida = a
            elif (len(bb) < len(aa)) & (len(bb) < len(cc)):
                print('La mejor lectura es Vertical')
                matrizLeida = b
            else:
                print('La mejor lectura es Horizontal')
                matrizLeida = c

        binario = p.finalProcess(matrizLeida)
        print(binario)
        print(len(binario))
        r = ((pow(tamaño,2)*8) - len(binario))/(pow(tamaño,2)*8)
        print(r*100)



if __name__ == "__main__":
    p = CodDPCM()
    '''matriz =    [[2,2,2,2,2],
                [12,22,2,2,2],
                [5,5,5,5,5],
                [5,5,5,5,5],
                [5,5,5,3,3]]
    '''

    matriz =    [[10,20,60],
                [30,50,70],
                [40,80,90]]

    tamaño = 3
    lectura = 4
    generar = False
    p.contacto(tamaño,lectura,generar,matriz)
    
    
   