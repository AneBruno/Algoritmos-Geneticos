from random import randint
from random import random

#variables
cantidad_pi=10
cantidad_genes=30
cromosomas_binario=[]
cromosomas_decimal=[]
lista_funcion_obj=[]
sumaFO=0
maxFO=0
minFO=0
promFO=0
cromosoma_maximo=[]
cromosoma_maximo_decimal=0
fitness=[]
prob_cross=0.75
prob_mut=0.05
punto_corte = 1
hijos=[]
corridas=2000

def crearPoblacionBinario():
 for x in range(cantidad_pi):
    cromosomas_binario.append([])
    for j in range(cantidad_genes):
        n=randint(0,1)
        cromosomas_binario[x].append(n)
def crearlistahijos():
    for x in range(cantidad_pi):
        hijos.append([])
        for j in range(cantidad_genes):
            hijos[x].append(0)


def convertirDecimal():
    for x in range(cantidad_pi):
        suma=0
        for j in range(cantidad_genes):
            if cromosomas_binario[x][j]==1:
                suma+=(2**(cantidad_genes-(j+1)))
        cromosomas_decimal[x]=suma
def crearListas():
    crearLista(10,cromosomas_decimal)
    crearLista(15,lista_funcion_obj)
    crearLista(30,cromosoma_maximo)
    crearLista(10,fitness)

def crearLista(a,lista):
    for x in range(a):
        lista.append(None)   
def calcularFuncionObjetivo():
    aux=0
    for i in range(cantidad_pi):
        aux= funcionObjetivo(cromosomas_decimal[i])
        lista_funcion_obj[i]=aux 
def funcionObjetivo(a):
  return  (a/((2**30)-1))**2
def calcularValores():
    suma=0
    maxi= lista_funcion_obj[0]
    maxc=cromosomas_binario[0]
    mini= lista_funcion_obj[0]
    minc=cromosomas_binario[0]
    for x in range(cantidad_pi):
        suma=suma + lista_funcion_obj[x]
        if(lista_funcion_obj[x]>=maxi):
            maxi=lista_funcion_obj[x]
            pos=x
        if(lista_funcion_obj[x]<= mini):
            mini=lista_funcion_obj[x]
    
    lista_funcion_obj[10]=suma
    lista_funcion_obj[11]=maxi
    lista_funcion_obj[12]=pos
    lista_funcion_obj[13]=mini
    lista_funcion_obj[14]=(suma/cantidad_pi)

def calcular_fitness():
    for i in range(cantidad_pi):
        x= (lista_funcion_obj[i]/sumaFO)
        fitness[i] = x
def crearRuleta():
    ruleta=[]
    acum=0
    for i in range(10):
        porc= fitness[i]*100
        for j in range(round(porc)):
            ruleta.append(i)
            acum+=1
    return ruleta
def crearHijos():
    crearlistahijos()
    fitness_elite=sorted(fitness,reverse=True)
    lista_porcentajes=[]
    cromosoma_nuevo_1=[0]*30
    cromosoma_nuevo_2=[0]*30
    lista_porcentajes= crearRuleta()
    mejor1=fitness_elite[0]
    mejor2=fitness_elite[1]
    for i in range(len(fitness)):
        if (fitness[i]==mejor1):
            hijos[0]=cromosomas_binario[i]
        elif (fitness[i]==mejor2):
            hijos[1]=cromosomas_binario[i]
    #print(lista_porcentajes)
    cont=0
    for i in range (0,8):
        y=randint(0,len(lista_porcentajes)-1)
        x= randint(0,len(lista_porcentajes)-1)
        for w in range(cantidad_genes):
            cromosoma_nuevo_1[w]=cromosomas_binario[lista_porcentajes[x]][w]
            cromosoma_nuevo_2[w]=cromosomas_binario[lista_porcentajes[y]][w]
        #print("cromosoma nuevo 1",cromosoma_nuevo_1)
        #print("cromosoma nuevo 2",cromosoma_nuevo_2)

        if (random() <= prob_cross): 
            crosover1=[5,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
            crosover2=[5,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
            
            crosover1[0]=cromosoma_nuevo_1[0]
            crosover2[0]=cromosoma_nuevo_2[0]
            
            for x in range (punto_corte,30):  #crossover desde el punto corte hasta fin
                crosover1[x]=cromosoma_nuevo_2[x]
                crosover2[x]=cromosoma_nuevo_1[x]
            #print("crosover")
            #print(crosover1)
            #print(crosover2)
            for m in range(cantidad_genes):
                cromosoma_nuevo_1[x]=crosover1[m]
                cromosoma_nuevo_2[x]=crosover2[m]
            #print("crosover copiado")
            #print(cromosoma_nuevo_1)
           # print(cromosoma_nuevo_2)

        if (random() <= prob_mut):
            x=randint(0,29)
            valor1=cromosoma_nuevo_1[x] #busco el valor 1 o 0 en esa posicion
            if (valor1==1):
             cromosoma_nuevo_1[x]=0
            else:
                cromosoma_nuevo_1[x]=1
            #print("mutacion  crosoma 1", x)
            #print(cromosoma_nuevo_1)
        if (random() <= prob_mut):
            x=randint(0,29)
            valor1=cromosoma_nuevo_2[x] #busco el valor 1 o 0 en esa posicion
            if (valor1==1):
             cromosoma_nuevo_2[x]=0
            else:
                cromosoma_nuevo_2[x]=1
            #print("mutacion  crosoma 2", x)
            #print(cromosoma_nuevo_2)
        hijos[i+2]=cromosoma_nuevo_1
        hijos[i+2]=cromosoma_nuevo_2  
        '''hijos[cont]=cromosoma_nuevo_1
        #print("hijo final ",hijos[cont])
        cont+=1
        hijos[cont]=cromosoma_nuevo_2
        #print("hijo final", hijos[cont])
        cont+=1   '''

                    
#main
crearListas()
crearPoblacionBinario()
for x in range(corridas):
    convertirDecimal()
    calcularFuncionObjetivo()
    calcularValores()
    sumaFO=lista_funcion_obj[10]
    maxFO=lista_funcion_obj[11]
    pos=lista_funcion_obj[12]
    for q in range(cantidad_genes):
        cromosoma_maximo[q]=cromosomas_binario[pos][q]
    cromosoma_maximo_decimal= cromosomas_decimal[lista_funcion_obj[12]]
    minFO=lista_funcion_obj[13]
    promFO= lista_funcion_obj[14]

    '''print("corrida",x+1)
    
    print("maximo FO", maxFO)
    print("minimo FO", minFO)
    print("cromosoma binario maximo", cromosoma_maximo)
    print("cromosoma decimal maximo ", cromosoma_maximo_decimal)'''
    print("promedio", promFO)
    calcular_fitness()
    crearHijos()
    for j in range(cantidad_pi):
        for s in range(cantidad_genes):
            cromosomas_binario[j][s]=hijos[j][s]
    #print(cromosomas_decimal)
