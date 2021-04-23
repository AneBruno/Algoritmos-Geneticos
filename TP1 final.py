import numpy as np 
import random 
import matplotlib.pyplot as plt
import pandas as pd

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

# Crea la poblacion inicial
def crearPoblacionInicial (cantPoblacionInicial):
    for _ in range (0,cantPoblacionInicial):
        binario = np.random.randint(2, size=30)
        poblacion.extend([Cromosoma(binario)])
        poblacionElite.extend([Cromosoma(binario)])
        poblacionRango.extend([Cromosoma(binario)])
    return poblacion

#calcula el fitness y las posiciones que ocuparan en la ruleta para toda la poblacion
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
            puntoCorte = (np.random.randint(1, 30))

            aux= np.random.randint(2, size=30)  

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
def crossoverelite (poblacion):
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
            puntoCorte = (np.random.randint(1, 30))

            aux= np.random.randint(2, size=30)  

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
def crossoverRango (poblacion):
    #----------RANGO--------------------
    poblacion = sorted(poblacion, key = lambda x : x.fitness, reverse=True) 
    hijos=[]
    for i in range(8):
        hijos.extend([poblacion[i]])
    #-----------CROSSOVER----------------
    rango = crearRango(poblacion)
    padre_1 = random.choice(rango)   
    padre_2 = random.choice(rango)
            
    if (random.random() <= prob_crossover):
        puntoCorte = (np.random.randint(1, 30))

        aux= np.random.randint(2, size=30)  

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

#crea una lista de cromosomas con los padres elejidos en seleccion rango
def crearRango(poblacion):
    rango=[]
    poblacion = sorted(poblacion, key = lambda x : x.fitness, reverse=True)
    for x in range (8):    
        rango.extend([poblacion[x].getBinario()])
    return rango
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
    aux = np.random.randint(2, size=30)      
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
    
#genera el grafico
def generarGrafico (prom,maxim,minim,titulo,l1,l2,l3):
    plt.plot(prom,'g', label = l1)
    plt.plot(maxim,'r',  label = l2)
    plt.plot(minim,'m' ,label = l3)
    plt.legend(loc="lower right")
    plt.ylim(0, 1.1)
    plt.title(titulo)
    plt.xlabel("Generacion")
    plt.ylabel("Funcion Objetivo")
    plt.show()
#guardamos en el excel maximos, minimos, etc de las poblaciones
def guardar_excel():
    lista_excel = []
    lista_excel.append(list(range(1,ciclos+2)))
    lista_excel.append(promedios)
    lista_excel.append(maximos)
    lista_excel.append(minimos)
    lista_excel.append(lista_cromosomas_maximo)
    lista_excel.append(promedios_elite)
    lista_excel.append(maximos_elite)
    lista_excel.append(minimos_elite)
    lista_excel.append(lista_crom_max_elite)
    lista_excel.append(promedios_rango)
    lista_excel.append(maximos_rango)
    lista_excel.append(minimos_rango)
    lista_excel.append(lista_crom_max_rango)
    df=pd.DataFrame(lista_excel)
    df = df.T
    df.columns = ['Corrida','Promedio FO','Maximo FO','Minimo FO','Cromosoma Máximo','Promedio FO Elite','Maximo FO Elite','Minimo FO Elite','Cromosoma Máximo Elite','Promedio FO Rango','Maximo FO Rango','Minimo FO Rango','Cromosoma Máximo Rango']
    with pd.ExcelWriter(ruta) as writer:
        df.to_excel(writer, sheet_name='TP 1', index=False)   
    print(df)

#variables
cantPoblacionInicial=10
prob_crossover=0.75
prob_mutacion=0.05
ciclos=199
promedios=[]
maximos=[]
minimos=[]
lista_cromosomas_maximo=[]
promedios_elite=[]
maximos_elite=[]
minimos_elite=[]
lista_crom_max_elite=[]
promedios_rango=[]
maximos_rango=[]
minimos_rango=[]
lista_crom_max_rango=[]
poblacion=[]
poblacionElite=[]
poblacionRango=[]
ruta= "C:\\Users\\Usuario\\Documents\\Algoritmos-Geneticos\\tp1.xlsx"

#programa principal
crearPoblacionInicial(cantPoblacionInicial)
tabla=[]
tablaelite=[]
tablarango=[]
tabla.extend([agregarTabla(poblacion)])
tablaelite.extend([agregarTabla(poblacionElite)])
tablarango.extend([agregarTabla(poblacionRango)])

for x in range (0,ciclos):
    calcularFitnessyposiciones(poblacion)
    calcularFitnessyposiciones(poblacionElite)
    calcularFitnessyposiciones(poblacionRango)
    poblacion=crossover(poblacion)
    poblacionElite=crossoverelite(poblacionElite)
    poblacionRango=crossoverRango(poblacionRango)
    tabla.extend([agregarTabla(poblacion)])
    tablaelite.extend([agregarTabla(poblacionElite)])
    tablarango.extend([agregarTabla(poblacionRango)])
   

for i in range(0, len(tabla)):
    promedios.append(tabla[i].getPromedio())
    maximos.append(tabla[i].getMaximo())
    minimos.append(tabla[i].getMinimo())
    lista_cromosomas_maximo.append(tabla[i].getCromosomaBinarioMaximo())
    promedios_elite.append(tablaelite[i].getPromedio())
    maximos_elite.append(tablaelite[i].getMaximo())
    minimos_elite.append(tablaelite[i].getMinimo())
    lista_crom_max_elite.append(tablaelite[i].getCromosomaBinarioMaximo())
    promedios_rango.append(tablarango[i].getPromedio())
    maximos_rango.append(tablarango[i].getMaximo())
    minimos_rango.append(tablarango[i].getMinimo())
    lista_crom_max_rango.append(tablarango[i].getCromosomaBinarioMaximo())

guardar_excel() 

generarGrafico(promedios,maximos,minimos,"Sin Elite","Promedio","Máximo","Mínimo")
generarGrafico(promedios_elite,maximos_elite,minimos_elite,"Con Elite","Promedio","Máximo","Mínimo")
generarGrafico(promedios_rango,maximos_rango,minimos_rango,"Método de Selección por Rango","Promedio","Máximo","Mínimo")
generarGrafico(promedios,promedios_elite,promedios_rango,"Comparación entre promedios","Sin Elite","Con Elite","Selección por Rango")