import numpy as np 
import random
import matplotlib.pyplot as plt

class Cromosoma:
    def __init__(self,binario):
        self.binario=binario
        self.decimal=convertirDecimal(binario)
        self.funcionObjetivo=calcularFuncionObjetivo(convertirDecimal(binario))
        self.fitness=-1.0
        self.posiciones=0
    def getFuncionObjetivo(self):
        return self.funcionObjetivo
    def getBinario(self):
        return self.binario
    def getFitness(self):
        return self.fitness
    def getDecimal(self):
        return self.decimal
    def getPosiciones(self):
        return self.posiciones
    def setFitness(self, fitness):
        self.fitness=fitness
    def setPosiciones(self,posiciones):
        self.posiciones=posiciones

class Tabla:
    def __init__(self,maximo,minimo,promedio,cromosomaBinarioMaximo,cromosomaDecimalMaximo):
        self.maximo=maximo
        self.minimo=minimo
        self.promedio=promedio
        self.cromosomaBinarioMaximo=cromosomaBinarioMaximo
        self.cromosomaDecimalMaximo=cromosomaDecimalMaximo
    def getMaximo(self):
        return self.maximo
    def getMinimo(self):
        return self.minimo
    def getPromedio(self):
        return self.promedio
    def getCromosomaBinarioMaximo(self):
        return self.cromosomaBinarioMaximo
    def getCromosomaDecimalMaximo(self):
        return self.cromosomaDecimalMaximo


# convierte binario a decimal, devuelve el decimal
def convertirDecimal (binario):
    suma=0
    for i in range (0,len(binario)):
        suma = suma+binario[i]*2**(len(binario)-1-i)
    return suma

# calcula la funcion objetivo seguen el decimal
def calcularFuncionObjetivo (decimal):
    return ((decimal/((2**30)-1))**2)

# Crea y retorna la poblacion inicial
def crearPoblacionInicial (cantPoblacionInicial):
    poblacion=[]
    for _ in range (0,cantPoblacionInicial):
        binario = np.random.randint(2, size=30)
        poblacion.extend([Cromosoma(binario)])
    return poblacion 

#calcula el fitness y las posiciones que ocuparan en la ruleta para toda la poblacion
def calcularFitnessyposiciones (poblacion):
    total = 0.0
    for x in range(0,len(poblacion)):
        total = total + poblacion[x].getFuncionObjetivo()
    for x in range(0,len(poblacion)):
        poblacion[x].setFitness(poblacion[x].getFuncionObjetivo()/total) 
        poblacion[x].setPosiciones(int(round(100*poblacion[x].getFitness())))
#primero hace elite, ordenamos la poblacion y elejimos los dos mejores
# elije dos padres al azar, le hace crossover y mutacion segun la probabilidad que salga
#devuelve los 10 hijos nuevos(2 de elite y 8 hijos)
def crossover (poblacion):
    #----------ELITE--------------------
    poblacion = sorted(poblacion, key = lambda x : x.fitness, reverse=True) 
    hijos=[]
    hijos.extend([poblacion[0],poblacion[1]])
    #-----------CROSSOVER----------------
    ruleta = crearRuleta(poblacion)
    
    for _ in range (0,int((len(poblacion)-2)/2)):
        padre_1 = random.choice(ruleta)   
        padre_2 = random.choice(ruleta)
                
        if (random.random() <= prob_crossover): 
               
            aux = [0]*30               
            for x in range (0,len(padre_2)):
                aux[x] = padre_2[x]

            for x in range (puntoCorte,len(padre_2)):  
                padre_2[x] = padre_1[x]
                padre_1[x] = aux[x]
      #---------MUTACION-----------------------  
        if (random.random() <= prob_mutacion): 
            padre_1 = hacerMutacion(padre_1)  
        if (random.random() <= prob_mutacion): 
            padre_2 = hacerMutacion(padre_2)
       
        hijos.extend([Cromosoma(padre_1),Cromosoma(padre_2)])
    return hijos

#agrega n cantidad de veces un cromosoma binario segun el fitness
# devuelve una lista (PD: el tamaño varia no siempre da 100)
def crearRuleta(poblacion):
    ruleta=[]
    for x in range (0,cantPoblacionInicial):
        aux=poblacion[x].getPosiciones()
        for _ in range (0,aux):     
            ruleta.extend([poblacion[x].getBinario()])
    return ruleta
# cambia un bit aleatorio del cromosoma por el opuesto 
def hacerMutacion (padre):
    aux = [0]*30      
    for x in range (len(padre)):
        aux[x]=padre[x]
    posicion = np.random.randint(0,len(aux)-1)
    if padre[posicion]==1:
        aux[posicion]=0
    else:
        aux[posicion]=1
    return aux
#genera una linea de la tabla y la retorna 
def agregarTabla (poblacion):
    poblacion = sorted(poblacion, key = lambda x : x.funcionObjetivo, reverse = True)  #Ordena los cromosomas de mayor funcionObjetivo a menor
    
    cromosomaBinarioMaximo=poblacion[0].getBinario() 
    cromosomaDecimalMaximo=poblacion[0].getDecimal()
    maximo=poblacion[0].getFuncionObjetivo()
    minimo=poblacion[len(poblacion)-1].getFuncionObjetivo()
    
    suma=0
    for x in range (0,len(poblacion)):
        suma=suma+poblacion[x].getFuncionObjetivo()
    promedio=suma/len(poblacion)

    lineaTabla=Tabla(maximo,minimo,promedio,cromosomaBinarioMaximo,cromosomaDecimalMaximo)
    
    return lineaTabla
    
# genera el grafico con los maximos, minimos y promedio
#verde=maximo, rojo=minimo, violeta/magenta=promedio
def generarGrafico (tabla):
    maximos=[]
    minimos=[]
    promedios=[]
    for x in range (0,len(tabla)):
        maximos.extend([tabla[x].getMaximo()])
        minimos.extend([tabla[x].getMinimo()])
        promedios.extend([tabla[x].getPromedio()])
    plt.plot(maximos,'g', linestyle='--',label = "Maximo")
    plt.plot(minimos,'r', linestyle='--', label = "Minimo")
    plt.plot(promedios,'m' , linestyle='--',label = "Promedio")
    plt.legend(loc="lower right")
    plt.ylim(0, 1.2)
    plt.xlabel("Generacion")
    plt.ylabel("Funcion Objetivo")
    plt.show()

#variables
ciclos=199
prob_crossover=0.75
prob_mutacion=0.05
puntoCorte=1
cantPoblacionInicial=10
#Programa principal
poblacion = crearPoblacionInicial(cantPoblacionInicial)
tabla=[]
tabla.extend([agregarTabla(poblacion)])
print("N°                      Cromosoma binario                       cromosoma decimal    maximoFO            minimoFO                promedioFO")
print("1  ",tabla[0].getCromosomaBinarioMaximo()," ",tabla[0].getCromosomaDecimalMaximo()," ",tabla[0].getMaximo(), " ", tabla[0].getMinimo(), " ", tabla[0].getPromedio())

for x in range (0,ciclos):
    calcularFitnessyposiciones(poblacion)
    poblacion=crossover(poblacion)
    tabla.extend([agregarTabla(poblacion)])
    print(x+2,'  ',tabla[x+1].getCromosomaBinarioMaximo()," ",tabla[x+1].getCromosomaDecimalMaximo()," ", tabla[x+1].getMaximo(), " ", tabla[x+1].getMinimo(), " ", tabla[x+1].getPromedio())
    
generarGrafico(tabla)