from random import randint
from random import random
from os import remove
import matplotlib.pyplot as plt
import pandas as pd
#variables
cantidad_pi=10
cantidad_genes=30
cromosomas_binario=[]
cromosomas_binario_elite=[]
cromosomas_binario_rango=[]
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
#punto_corte = 1
hijos=[]
corridas=20
hijos_elite=[]
hijos_rango=[]
fitness_elite=[]
fitness_rango=[]
promedios=[]
lista_cromosomas_maximo=[]
maximos=[]
minimos=[]
lista_crom_max_elite=[]
maximos_elite=[]
minimos_elite=[]
promedios_elite=[]
lista_crom_max_rango=[]
maximos_rango=[]
minimos_rango=[]
promedios_rango=[]
lista_cromosomas_maximo_bin=[]
lista_crom_max_bin_elite=[]
lista_crom_max_bin_rango=[]

def crearPoblacionBinario():
 for x in range(cantidad_pi):
    cromosomas_binario_elite.append([])
    cromosomas_binario_rango.append([])
    cromosomas_binario.append([])
    for j in range(cantidad_genes):
        n=randint(0,1)
        cromosomas_binario_rango[x].append(n)
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
def crearlistahijos_rango():
    for x in range(cantidad_pi):
        hijos_rango.append([])
        for j in range(cantidad_genes):
            hijos_rango[x].append(0)
def convertirDecimal(lista_bin):
    for x in range(cantidad_pi):
        suma=0
        for j in range(cantidad_genes):
            if lista_bin[x][j]==1:
                suma+=(2**(cantidad_genes-(j+1)))
        cromosomas_decimal[x]=suma
def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
def crearListas():
    crearLista(10,cromosomas_decimal)
    crearLista(15,lista_funcion_obj)
    crearLista(30,cromosoma_maximo)
    crearLista(10,fitness)
    crearLista(10,fitness_elite)
    crearLista(10,fitness_rango)
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
            punto_corte=randint(0,cantidad_genes-1)
            for x in range (1,30):  #crossover desde el punto corte hasta fin
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
            #print(cromosoma_nuevo_2)

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
    cont=2
    for i in range (0,4):
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
            punto_corte=randint(0,cantidad_genes-1)    
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
        hijos_elite[cont]=cromosoma_nuevo_1
        cont+=1
        hijos_elite[cont]=cromosoma_nuevo_2 
        cont+=1 
def crearHijos_rango():
    crearlistahijos_rango()
    fitness_rango=sorted(fitness,reverse=True)
    mejores_rango=[]
    crearLista(cantidad_pi,mejores_rango)
    
    for i in range(8):
        mejores_rango[i]=fitness_rango[i]
    
    for i in range(8):
        for j in range(len(fitness)):
             if(mejores_rango[i]== fitness[j]):
                hijos_rango[i]= cromosomas_binario_rango[j]
    lista_porcentajes=[]
    cromosoma_nuevo_1=[0]*30
    cromosoma_nuevo_2=[0]*30
    lista_porcentajes= crearRuleta()
    
    y=randint(0,len(lista_porcentajes)-1)
    x= randint(0,len(lista_porcentajes)-1)
    for w in range(cantidad_genes):
        cromosoma_nuevo_1[w]=cromosomas_binario_rango[lista_porcentajes[x]][w]
        cromosoma_nuevo_2[w]=cromosomas_binario_rango[lista_porcentajes[y]][w]
        #print("cromosoma nuevo 1",cromosoma_nuevo_1)
        #print("cromosoma nuevo 2",cromosoma_nuevo_2)

    if (random() <= prob_cross): 
        crossover1=[0]*30
        crossover2=[0]*30
                
        crossover1[0]=cromosoma_nuevo_1[0]
        crossover2[0]=cromosoma_nuevo_2[0]
        punto_corte=randint(0,cantidad_genes-1)       
        for x in range (punto_corte,30):  #crossover desde el punto corte hasta fin
            crossover1[x]=cromosoma_nuevo_2[x]
            crossover2[x]=cromosoma_nuevo_1[x]
                
        for m in range(cantidad_genes):
            cromosoma_nuevo_1[x]=crossover1[m]
            cromosoma_nuevo_2[x]=crossover2[m]
                
    if (random() <= prob_mut):
        x=randint(0,29)
        valor1=cromosoma_nuevo_1[x] #busco el valor 1 o 0 en esa posicion
        if (valor1==1):
            cromosoma_nuevo_1[x]=0
        else:
            cromosoma_nuevo_1[x]=1
            
    if (random() <= prob_mut):
        x=randint(0,29)
        valor1=cromosoma_nuevo_2[x] #busco el valor 1 o 0 en esa posicion
        if (valor1==1):
            cromosoma_nuevo_2[x]=0
        else:
            cromosoma_nuevo_2[x]=1
      
    hijos_rango[8]=cromosoma_nuevo_1
    hijos_rango[9]=cromosoma_nuevo_2 
def graficar(prom,maxim,minim,tit,l1,l2,l3):
    x1=range(1,(corridas+1))
    plt.plot(x1,prom,label=l1)
    plt.plot(x1,maxim,label=l2)
    plt.plot(x1,minim,label=l3)
    plt.ylim(0, 1.1)
    plt.title(tit)
    plt.xlabel('Corridas')
    plt.ylabel('Valores Función Objetivo')
    plt.legend()
    plt.show()    
ruta= "C:\\Users\\Usuario\\Documents\\Algoritmos-Geneticos\\tp1.xlsx"

crearListas()
crearPoblacionBinario()

for x in range(corridas):
    convertirDecimal(cromosomas_binario)
    calcularFuncionObjetivo()
    calcularValores(cromosomas_binario)
    sumaFO=lista_funcion_obj[10]
    maxFO=lista_funcion_obj[11]
    #max_str=str(maxFO)
    maximos.append(maxFO)
    pos=lista_funcion_obj[12]
    for q in range(cantidad_genes):
        cromosoma_maximo[q]=cromosomas_binario[pos][q]
    cromosoma_maximo_decimal= cromosomas_decimal[lista_funcion_obj[12]]
    #crom_str=str(cromosoma_maximo_decimal)
    lista_cromosomas_maximo.append(cromosoma_maximo_decimal)
    lista_cromosomas_maximo_bin.append(binarizar(cromosoma_maximo_decimal))
    lista_cromosomas_maximo_bin
    minFO=lista_funcion_obj[13]
    #min_str=str(minFO)
    minimos.append(minFO)
    promFO= lista_funcion_obj[14]
    calcular_fitness()
    crearHijos()
    for j in range(cantidad_pi):
        for s in range(cantidad_genes):
            cromosomas_binario[j][s]=hijos[j][s]     
    #prom_str=str(promFO)
    promedios.append(promFO) 

for x in range(corridas):
    convertirDecimal(cromosomas_binario_elite)
    calcularFuncionObjetivo()
    calcularValores(cromosomas_binario_elite)
    sumaFO=lista_funcion_obj[10]
    maxFO=lista_funcion_obj[11]
    #max_str=str(maxFO)
    maximos_elite.append(maxFO)
    pos=lista_funcion_obj[12]
    for q in range(cantidad_genes):
        cromosoma_maximo[q]=cromosomas_binario_elite[pos][q]
    cromosoma_maximo_decimal= cromosomas_decimal[lista_funcion_obj[12]]
    #crom_str=str(cromosoma_maximo_decimal)
    lista_crom_max_elite.append(cromosoma_maximo_decimal)
    minFO=lista_funcion_obj[13]
    #min_str=str(minFO)
    minimos_elite.append(minFO)
    promFO= lista_funcion_obj[14]
    #prom_str=str(promFO)
    promedios_elite.append(promFO)
    calcular_fitness()
    crearHijos_elite()
    for j in range(cantidad_pi):
        for s in range(cantidad_genes):
            cromosomas_binario_elite[j][s]=hijos_elite[j][s] 
    
for x in range(corridas):
    convertirDecimal(cromosomas_binario_rango)
    calcularFuncionObjetivo()
    calcularValores(cromosomas_binario_rango)
    sumaFO=lista_funcion_obj[10]
    maxFO=lista_funcion_obj[11]
    #max_str=str(maxFO)
    maximos_rango.append(maxFO)
    pos=lista_funcion_obj[12]
    for q in range(cantidad_genes):
        cromosoma_maximo[q]=cromosomas_binario_rango[pos][q]
    cromosoma_maximo_decimal= cromosomas_decimal[lista_funcion_obj[12]]
    #crom_str=str(maxFO)
    lista_crom_max_rango.append(cromosoma_maximo_decimal)
    minFO=lista_funcion_obj[13]
    #min_str=str(minFO)
    minimos_rango.append(minFO)
    promFO= lista_funcion_obj[14]
    #prom_str=str(promFO)
    promedios_rango.append(promFO)
    calcular_fitness()
    crearHijos_rango()
    for j in range(cantidad_pi):
        for s in range(cantidad_genes):
            cromosomas_binario_rango[j][s]=hijos_rango[j][s] 
    
lista_excel = []
lista_excel.append(list(range(1,corridas+1)))
lista_excel.append(promedios)
lista_excel.append(maximos)
lista_excel.append(minimos)
lista_excel.append(lista_cromosomas_maximo)
lista_excel.append(lista_cromosomas_maximo_bin)
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
df.columns = ['Corrida','Promedio FO','Maximo FO','Minimo FO','Cromosoma Máximo','Cromosoma Máximo Bin','Promedio FO Elite','Maximo FO Elite','Minimo FO Elite','Cromosoma Máximo Elite','Promedio FO Rango','Maximo FO Rango','Minimo FO Rango','Cromosoma Máximo Rango']
with pd.ExcelWriter(ruta) as writer:
    df.to_excel(writer, sheet_name='TP 1', index=False)

graficar(promedios,maximos,minimos,"Sin Elite","Promedio","Máximo","Mínimo")
#if (corridas>20):
graficar(promedios_elite,maximos_elite,minimos_elite,"Con Elite","Promedio","Máximo","Mínimo")
graficar(promedios_rango,maximos_rango,minimos_rango,"Método de Selección por Rango","Promedio","Máximo","Mínimo")
graficar(promedios,promedios_elite,promedios_rango,"Comparación entre promedios","Sin Elite","Con Elite","Selección por Rango")

print(df)