from random import randint
from random import random

#variables
cantidad_pi=10
cantidad_genes=30
cromosomas_binario=[]
cromosomas_binario_elite=[]
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
corridas=30
hijos_elite=[]
fitness_elite=[]
cromosomas_binario_elite=[]
cromosomas_decimal_elite=[]

def crearPoblacionBinario():
 for x in range(cantidad_pi):
    cromosomas_binario_elite.append([])
    cromosomas_binario.append([])
    for j in range(cantidad_genes):
        n=randint(0,1)
        cromosomas_binario_elite[x].append(n)
        cromosomas_binario[x].append(n)
def crearlistahijos():
    for x in range(cantidad_pi):
        hijos.append([])
        for j in range(cantidad_genes):
            hijos[x].append(0)
def crearlistahijos_elite():
    for x in range(cantidad_pi):
        hijos_elite.append([])
        for j in range(cantidad_genes):
            hijos_elite[x].append(0)

def convertirDecimal(lista_bin):
    for x in range(cantidad_pi):
        suma=0
        for j in range(cantidad_genes):
            if lista_bin[x][j]==1:
                suma+=(2**(cantidad_genes-(j+1)))
        cromosomas_decimal[x]=suma

def crearListas():
    crearLista(10,cromosomas_decimal)
    crearLista(15,lista_funcion_obj)
    crearLista(30,cromosoma_maximo)
    crearLista(10,fitness)
    crearLista(10,fitness_elite)
def crearLista(a,lista):
    for x in range(a):
        lista.append(None)   
def calcularFuncionObjetivo():
    aux=0
    i=0
    for i in range(cantidad_pi):
        aux= funcionObjetivo(cromosomas_decimal[i])
        lista_funcion_obj[i]=aux 
def funcionObjetivo(a):
  return  (a/((2**30)-1))**2
def calcularValores(lista_bin):
    suma=0
    maxi= lista_funcion_obj[0]
    maxc=lista_bin[0]
    mini= lista_funcion_obj[0]
    minc=lista_bin[0]
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
    lista_porcentajes=[]
    cromosoma_nuevo_1=[0]*30
    cromosoma_nuevo_2=[0]*30
    lista_porcentajes= crearRuleta()
    #print(lista_porcentajes)
    cont=0
    for i in range (0,int(len(cromosomas_decimal)/2)):
        y=randint(0,len(lista_porcentajes)-1)
        x= randint(0,len(lista_porcentajes)-1)
        for w in range(cantidad_genes):
            cromosoma_nuevo_1[w]=cromosomas_binario[lista_porcentajes[x]][w]
            cromosoma_nuevo_2[w]=cromosomas_binario[lista_porcentajes[y]][w]
        #print("cromosoma nuevo 1",cromosoma_nuevo_1)
        #print("cromosoma nuevo 2",cromosoma_nuevo_2)

        if (random() <= prob_cross): 
            crossover1=[0]*30
            crossover2=[0]*30
            
            crossover1[0]=cromosoma_nuevo_1[0]
            crossover2[0]=cromosoma_nuevo_2[0]
            
            for x in range (punto_corte,30):  #crossover desde el punto corte hasta fin
                crossover1[x]=cromosoma_nuevo_2[x]
                crossover2[x]=cromosoma_nuevo_1[x]
            #print("crosover")
            #print(crosover1)
            #print(crosover2)
            for m in range(cantidad_genes):
                cromosoma_nuevo_1[x]=crossover1[m]
                cromosoma_nuevo_2[x]=crossover2[m]
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

        hijos[cont]=cromosoma_nuevo_1
        #print("hijo final ",hijos[cont])
        cont+=1
        hijos[cont]=cromosoma_nuevo_2
        #print("hijo final", hijos[cont])
        cont+=1   
def crearHijos_elite():
    crearlistahijos_elite()
    fitness_elite=sorted(fitness,reverse=True)
    lista_porcentajes=[]
    cromosoma_nuevo_1=[0]*30
    cromosoma_nuevo_2=[0]*30
    lista_porcentajes= crearRuleta()
    mejor1=fitness_elite[0]
    mejor2=fitness_elite[1]
    for i in range(len(fitness)):
        if (fitness[i]==mejor1):
            hijos_elite[0]=cromosomas_binario_elite[i]
        elif (fitness[i]==mejor2):
            hijos_elite[1]=cromosomas_binario_elite[i]
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
            crossover1=[0]*30
            crossover2=[0]*30
                
            crossover1[0]=cromosoma_nuevo_1[0]
            crossover2[0]=cromosoma_nuevo_2[0]
                
            for x in range (punto_corte,30):  #crossover desde el punto corte hasta fin
                crossover1[x]=cromosoma_nuevo_2[x]
                crossover2[x]=cromosoma_nuevo_1[x]
                #print("crosover")
                #print(crosover1)
                #print(crosover2)
            for m in range(cantidad_genes):
                cromosoma_nuevo_1[x]=crossover1[m]
                cromosoma_nuevo_2[x]=crossover2[m]
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
        hijos_elite[i+2]=cromosoma_nuevo_1
        hijos_elite[i+2]=cromosoma_nuevo_2  
def limpiar(): 
    lista_funcion_obj.clear()
    sumaFO=0
    maxFO=0
    minFO=0
    promFO=0
    cromosoma_maximo.clear()
    cromosoma_maximo_decimal=0
    fitness.clear()                 
#main
crearListas()
crearPoblacionBinario()
for x in range(corridas):
    convertirDecimal(cromosomas_binario)
    calcularFuncionObjetivo()
    calcularValores(cromosomas_binario)
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
    
    calcular_fitness()
    crearHijos()
    for j in range(cantidad_pi):
        for s in range(cantidad_genes):
            cromosomas_binario[j][s]=hijos[j][s]     
    print("promedio", promFO) 
print()
#fitness.clear()
for x in range(corridas):
    convertirDecimal(cromosomas_binario_elite)
    calcularFuncionObjetivo()
    calcularValores(cromosomas_binario_elite)
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
    
    calcular_fitness()
    crearHijos_elite()
    for j in range(cantidad_pi):
        for s in range(cantidad_genes):
            cromosomas_binario_elite[j][s]=hijos_elite[j][s] 
    print("promedio elite", promFO)    