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

class Cromosoma_Elite:
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

class Cromosoma_Rango:
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
def crearPoblacionInicialElite (cantPoblacionInicial):
    poblacion_elite=[]
    for _ in range (0,cantPoblacionInicial):
        binario = np.random.randint(2, size=30)
        poblacion_elite.extend([Cromosoma_Elite(binario)])
    return poblacion_elite
def crearPoblacionInicialRango  (cantPoblacionInicial):
    poblacion_rango=[]
    for _ in range (0,cantPoblacionInicial):
        binario = np.random.randint(2, size=30)
        poblacion_rango.extend([Cromosoma_Elite(binario)])
    return poblacion_rango
    
#calcula el fitness y las posiciones que ocupara en la ruleta para toda la poblacion
def calcularFitnessyposiciones (poblacion):
    total = 0.0
    for x in range(0,len(poblacion)):
        total = total + poblacion[x].getFuncionObjetivo()
    for x in range(0,len(poblacion)):
        poblacion[x].setFitness(poblacion[x].getFuncionObjetivo()/total) 
        poblacion[x].setPosiciones(int(round(100*poblacion[x].getFitness())))

# elije dos padres al azar, le hace crossover y mutacion segun la probabilidad que salga
#devuelve los 10 hijos nuevos
def crossover (poblacion):
    #-------------CROSSOVER-------------
    ruleta = crearRuleta(poblacion)
    hijos = []
    for _ in range (0,int(len(poblacion)/2)):
        padre_1 = random.choice(ruleta)   
        padre_2 = random.choice(ruleta)
                
        if (random.random() <= prob_crossover): 
               
            aux = [0]*30               
            for x in range (0,len(padre_2)):
                aux[x] = padre_2[x]
        
            for x in range (puntoCorte,len(padre_2)):  
                padre_2[x] = padre_1[x]
                padre_1[x] = aux[x]
        #-------------MUTACION----------------------
        if (random.random() <= prob_mutacion): 
            padre_1 = hacerMutacion(padre_1)  
        if (random.random() <= prob_mutacion): 
            padre_2 = hacerMutacion(padre_2)
       
        hijos.extend([Cromosoma(padre_1),Cromosoma(padre_2)])
    return hijos

def crossover_elite (poblacion_elite):
    #----------ELITE--------------------
    poblacion_elite = sorted(poblacion_elite, key = lambda x : x.fitness, reverse=True) 
    hijos_elite=[]
    hijos_elite.extend([poblacion_elite[0],poblacion_elite[1]])
    #-----------CROSSOVER----------------
    ruleta = crearRuleta(poblacion_elite)
    
    for _ in range (0,int((len(poblacion_elite)-2)/2)):
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
       
        hijos_elite.extend([Cromosoma(padre_1),Cromosoma(padre_2)])
    return hijos_elite

def crossover_rango (poblacion_rango):
    poblacion_rango = sorted(poblacion_rango, key = lambda x : x.fitness, reverse=True) 
    hijos_rango=[]
    hijos_rango.extend([poblacion_rango[0],poblacion_rango[1],poblacion_rango[2],poblacion_rango[3],poblacion_rango[4],poblacion_rango[5],poblacion_rango[6],poblacion_rango[7]])
    #-----------CROSSOVER----------------
    ruleta = crearRuleta(poblacion_rango)
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
       
    hijos_rango.extend([Cromosoma_Rango(padre_1),Cromosoma_Rango(padre_2)])
    return hijos_rango
#agrega n cantidad de veces un cromosoma binario segun el fitness
# devuelve una lista 
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
    
    maximo=poblacion[0].getFuncionObjetivo()
    cromosomaBinarioMaximo=poblacion[0].getBinario() 
    minimo=poblacion[len(poblacion)-1].getFuncionObjetivo()
    cromosomaDecimalMaximo=poblacion[0].getDecimal()
    
    suma=0
    for x in range (0,len(poblacion)):
        suma=suma+poblacion[x].getFuncionObjetivo()
    promedio=suma/len(poblacion)

    lineaTabla=Tabla(maximo,minimo,promedio,cromosomaBinarioMaximo,cromosomaDecimalMaximo)
    
    return lineaTabla
  
# Imprime una tabla con el maximo funcionObjetivo, minimo funcionObjetivo, y promedio de todos los 
# valores para cada generacion
def generarGrafico (tabla,titulo):
    maximos=[]
    minimos=[]
    promedios=[]
    for x in range (0,len(tabla)):
        maximos.extend([tabla[x].getMaximo()])
        minimos.extend([tabla[x].getMinimo()])
        promedios.extend([tabla[x].getPromedio()])
    plt.plot(maximos,'g', label = "Maximo")
    plt.plot(minimos,'r',  label = "Minimo")
    plt.plot(promedios,'m' ,label = "Promedio")
    plt.legend(loc="lower right")
    plt.ylim(0, 1.1)
    plt.title(titulo)
    plt.xlabel("Generacion")
    plt.ylabel("Funcion Objetivo")
    plt.show()

#variables

cantPoblacionInicial=10
prob_crossover=0.75
prob_mutacion=0.05
puntoCorte=1
ciclos=199
#programa principal
poblacion = crearPoblacionInicial(cantPoblacionInicial)
poblacion_elite = crearPoblacionInicialElite(cantPoblacionInicial)
poblacion_rango = crearPoblacionInicialRango(cantPoblacionInicial)
tabla=[]
tabla_elite=[]
tabla_rango=[]
tabla.extend([agregarTabla(poblacion)])
tabla_elite.extend([agregarTabla(poblacion_elite)])
tabla_rango.extend([agregarTabla(poblacion_rango)])
print("N°                      Cromosoma binario                       cromosoma decimal    maximoFO            minimoFO                promedioFO")
print("1  ",tabla[0].getCromosomaBinarioMaximo()," ",tabla[0].getCromosomaDecimalMaximo()," ",tabla[0].getMaximo(), " ", tabla[0].getMinimo(), " ", tabla[0].getPromedio())

for x in range (0,ciclos):
    calcularFitnessyposiciones(poblacion)
    poblacion=crossover(poblacion)
    tabla.extend([agregarTabla(poblacion)])
    print(x+2,'  ',tabla[x+1].getCromosomaBinarioMaximo()," ",tabla[x+1].getCromosomaDecimalMaximo()," ", tabla[x+1].getMaximo(), " ", tabla[x+1].getMinimo(), " ", tabla[x+1].getPromedio())
    calcularFitnessyposiciones(poblacion_elite)
    poblacion_elite=crossover_elite(poblacion_elite)
    tabla_elite.extend([agregarTabla(poblacion_elite)])
    print(x+2,'  ',tabla_elite[x+1].getCromosomaBinarioMaximo()," ",tabla_elite[x+1].getCromosomaDecimalMaximo()," ", tabla_elite[x+1].getMaximo(), " ", tabla_elite[x+1].getMinimo(), " ", tabla_elite[x+1].getPromedio())
    calcularFitnessyposiciones(poblacion_rango)
    poblacion_rango=crossover_rango(poblacion_rango)
    tabla_rango.extend([agregarTabla(poblacion_rango)])
    print(x+2,'  ',tabla_rango[x+1].getCromosomaBinarioMaximo()," ",tabla_rango[x+1].getCromosomaDecimalMaximo()," ", tabla_rango[x+1].getMaximo(), " ", tabla_rango[x+1].getMinimo(), " ", tabla_rango[x+1].getPromedio())

generarGrafico(tabla,'Sin Elite')
generarGrafico(tabla_elite, 'Con elite')
generarGrafico(tabla_rango, 'Metodo de Seleccion Por Rango')