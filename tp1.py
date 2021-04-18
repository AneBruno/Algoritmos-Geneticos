from random import randint
from random import random

n=0
cantidad_pi=10
cantidad_genes=30
cantidad_ciclos=100
cromosomas_binario=[]
cromosomas_decimal=[]
lista_funcion_obj=[]
lista_porcentajes=[]
fitness=[]
prob_cross=0.75
prob_mut=0.05
padres=[]
probabilidades=[]
cromosomas_hijo=[]
punto_corte = 1
hijos=[] #tiene la nueva poblacion, con crossover o con mutación
poblacion_elite=[]
fitness_elite=[]
hijos_elite=[]
fitness_rango=[]
hijos_rango=[]
hijos_m=[]


def crearPoblacionBinario():
 for x in range(cantidad_pi):
    cromosomas_binario.append([])
    for j in range(cantidad_genes):
        n=randint(0,1)
        cromosomas_binario[x].append(n) 

def crearlistahijos():
    for x in range(cantidad_pi):
        hijos_m.append([])
        for j in range(cantidad_genes):
            hijos_m[x].append(0)

def crearLista(a,lista):
    for x in range(a):
        lista.append(None)

def convertirDecimal():
    for x in range(cantidad_pi):
        suma=0
        for j in range(cantidad_genes):
            if cromosomas_binario[x][j]==1:
                suma+=(2**(cantidad_genes-(j+1)))
        cromosomas_decimal[x]=suma

def funcionObjetivo(a):
  return  (a/((2**30)-1))**2

def calculaSPM():
    suma=0
    maxi=lista_funcion_obj[0]
    mini=lista_funcion_obj[0]
    for x in range(cantidad_pi):
        suma+=lista_funcion_obj[x]
        if (lista_funcion_obj[x]>= maxi):
            maxi=lista_funcion_obj[x]
            nro_max=cromosomas_decimal[x] #el nro decimal que me genera el valor de f. objt. mas grande lo guardo en nro_max
        if (lista_funcion_obj[x]<= mini):
            mini=lista_funcion_obj[x]
    lista_funcion_obj[cantidad_pi]=suma
    lista_funcion_obj[cantidad_pi+1]=maxi
    lista_funcion_obj[cantidad_pi+2]=nro_max
    lista_funcion_obj[cantidad_pi+3]= (suma/cantidad_pi)
    lista_funcion_obj[cantidad_pi+4]= mini

#calculo el fitness de cada cromosoma 
def calcular_fitness(suma,maxi,mini):
    for i in range(10):
        x= (lista_funcion_obj[i]/suma)
        fitness[i] = x

def porcentajes(lista_porcentajes):
    acum=0
    for i in range(10):
        porc= fitness[i]*100
        for j in range(round(porc)):
            lista_porcentajes[acum] = i
            acum+=1
            if(acum==100):
                break
    return acum

def hacer_crossover(acum):
    #crearLista(cantidad_genes,cromosomas_hijo)
    padre1=[]
    padre2=[]
    for i in range (0,int(len(cromosomas_decimal)/2)):
        x= randint(0,acum)
        cromosoma_nuevo_1=cromosomas_binario[lista_porcentajes[x]]
        y=randint(0,acum)
        cromosoma_nuevo_2=cromosomas_binario[lista_porcentajes[y]]
        '''print('padre1')
        print(cromosoma_nuevo_1)
        print('padre2')
        print(cromosoma_nuevo_2)'''
        
        if (random() <= prob_cross): 
            aux=[]
            crearLista(30,aux)            
            for x in range (0,len(padre2)):
                aux[x] = cromosoma_nuevo_2[x]
            for x in range (punto_corte,len(padre2)):  #crossover desde el punto corte hasta fin
                cromosoma_nuevo_2[x] = cromosoma_nuevo_1[x]
                cromosoma_nuevo_1[x] = aux[x]
            '''print('hijo1')
            print(cromosoma_nuevo_1)
            print('hijo2')
            print(cromosoma_nuevo_2)'''
            
        if (random() <= prob_mut):
            x=randint(0,29)
            valor1=cromosoma_nuevo_1[x] #busco el valor 1 o 0 en esa posicion
            if (valor1==1):
                cromosoma_nuevo_1[x]==0
            else:
                cromosoma_nuevo_1[x]==1

        if (random() <= prob_mut):
            y=randint(0,29)
            valor2=cromosoma_nuevo_2[y]
            if(valor2==1):
                cromosoma_nuevo_2[y]==0
            else:
                cromosoma_nuevo_2==1

        hijos.append(cromosoma_nuevo_1)
        hijos.append(cromosoma_nuevo_2)              

def generar_pob_elite():
    fitness_elite=sorted(fitness,reverse=True)
    #test
    mejor1=fitness_elite[0]
    mejor2=fitness_elite[1]
    for i in range(len(fitness)):
        if (fitness[i]==mejor1):
            hijos_elite[0]=cromosomas_binario[i]
        elif (fitness[i]==mejor2):
            hijos_elite[1]=cromosomas_binario[i]
    '''print('padre elite 1')
    print(hijos_elite[0])
    print ('padre elite 2')
    print(hijos_elite[1])'''

    #elijo solo 8 porque dos son los padres (int(len(cromosomas_decimal)/2)-2)
    for i in range (0,8):
        x= randint(0,acum)
        cromosoma_nuevo_1=cromosomas_binario[lista_porcentajes[x]]
        y=randint(0,acum)
        cromosoma_nuevo_2=cromosomas_binario[lista_porcentajes[y]]
        '''print('padre1')
        print(cromosoma_nuevo_1)
        print('padre2')
        print(cromosoma_nuevo_2)'''
        
        if (random() <= prob_cross): 
            aux=[]
            crearLista(30,aux)            
            for x in range (30):
                aux[x] = cromosoma_nuevo_2[x]
            for x in range (punto_corte,29):  #crossover desde el punto corte hasta fin
                cromosoma_nuevo_2[x] = cromosoma_nuevo_1[x]
                cromosoma_nuevo_1[x] = aux[x]
            '''print('hijo1')
            print(cromosoma_nuevo_1)
            print('hijo2')
            print(cromosoma_nuevo_2)'''
            
        if (random() <= prob_mut):
            x=randint(0,29)
            valor1=cromosoma_nuevo_1[x] #busco el valor 1 o 0 en esa posicion
            if (valor1==1):
                cromosoma_nuevo_1[x]==0
            else:
                cromosoma_nuevo_1[x]==1

        if (random() <= prob_mut):
            y=randint(0,29)
            valor2=cromosoma_nuevo_2[y]
            if(valor2==1):
                cromosoma_nuevo_2[y]==0
            else:
                cromosoma_nuevo_2==1
        hijos_elite[i+2]=cromosoma_nuevo_1
        hijos_elite[i+2]=cromosoma_nuevo_2  
      
def generar_pob_rango():
    fitness_rango=sorted(fitness,reverse=True)
    mejores_rango=[]
    crearLista(cantidad_pi,mejores_rango)
    for i in range(8):
        mejores_rango[i]=fitness_rango[i]

    for i in range(8):
        for j in range(len(fitness)):
             if(mejores_rango[i]== fitness[j]):
                hijos_rango[i]= cromosomas_binario[j]
    print('MEJORES RANGO')
    print(mejores_rango)
            
    x= randint(0,8)
    cromosoma_nuevo_1=cromosomas_binario[lista_porcentajes[x]]
    y=randint(0,8)
    cromosoma_nuevo_2=cromosomas_binario[lista_porcentajes[y]]
                
    if (random() <= prob_cross): 
        aux=[]
        crearLista(30,aux)            
        for x in range (30):
            aux[x] = cromosoma_nuevo_2[x]
        for x in range (punto_corte,29):  #crossover desde el punto corte hasta fin
            cromosoma_nuevo_2[x] = cromosoma_nuevo_1[x]
            cromosoma_nuevo_1[x] = aux[x]
            '''print('hijo1')
            print(cromosoma_nuevo_1)
            print('hijo2')
            print(cromosoma_nuevo_2)'''
                    
    if (random() <= prob_mut):
        x=randint(0,29)
        valor1=cromosoma_nuevo_1[x] #busco el valor 1 o 0 en esa posicion
        if (valor1==1):
            cromosoma_nuevo_1[x]==0
        else:
            cromosoma_nuevo_1[x]==1

            if (random() <= prob_mut):
                y=randint(0,29)
                valor2=cromosoma_nuevo_2[y]
            if(valor2==1):
                cromosoma_nuevo_2[y]==0
            else:
                cromosoma_nuevo_2==1

            '''print('padre elite 1')
            print(hijos_elite[0])
            print ('padre elite 2')
            print(hijos_elite[1])'''

    hijos_rango[8]=cromosoma_nuevo_1
    hijos_rango[9]=cromosoma_nuevo_2  
            
def pasar_poblacion():
    x_pob =[]
    for i in range (cantidad_pi):
        crearlistahijos()
        x_pob = list(hijos[i])
        #print (x_pob)
        for j in range(cantidad_genes):
            cromosomas_binario[i][j] = x_pob[j]
    
#MAIN
crearLista(cantidad_pi, cromosomas_decimal)
crearLista(cantidad_pi,fitness)
crearLista((cantidad_pi+5),lista_funcion_obj)
crearLista(100,lista_porcentajes)
crearLista(cantidad_pi,padres)
crearLista(cantidad_pi,fitness_elite)
crearLista(cantidad_pi,hijos_elite) 
crearLista(cantidad_pi, fitness_rango) 
crearLista(cantidad_pi,hijos_rango) 


crearPoblacionBinario()
for i in range (cantidad_ciclos):
    convertirDecimal()
    for x in range(cantidad_pi):
        lista_funcion_obj[x]= funcionObjetivo(cromosomas_decimal[x])
    nro_max=0
    calculaSPM()
    suma= lista_funcion_obj[10]
    maxi= lista_funcion_obj[11]
    nro_max= lista_funcion_obj[12]
    prom = lista_funcion_obj[13]
    mini= lista_funcion_obj[14]
    calcular_fitness(suma,maxi,prom)
    acum= porcentajes(lista_porcentajes)
    hacer_crossover(acum)
    print('promedio',prom)
    pasar_poblacion()
    #ELITISMO 
    #generar_pob_elite()
    #Otro metodo de seleccion - RANGO 
    #generar_pob_rango()
    
    
'''print('\nFUNCION OBJETIVO')
for i in range (10):
    print(lista_funcion_obj[i])

print('\nSUMA:', end=" ") 
print(suma)
print('MAXIMO:', end=" ") 
print(maxi)
print('Cromosoma que genera el valor máximo:', end=" ") 
print(nro_max)
print('MINIMO:', end=" ") 
print(mini)
print('PROMEDIO:', end=" ") 
print(prom)

print('\nFITNESS')
for i in range (len(fitness)):
    print(fitness[i])
sumafitnees=0
for i in range (len(fitness)):
    sumafitnees+=fitness[i]
print (sumafitnees)

print('\nPOOL GENERADO:')
print(lista_porcentajes)
#print(len(lista_porcentajes))
print('ACUMULADOR DEL POOL: ', end=" ")
print(acum)
#print(padres)
#print(probabilidades)
print('\nPOBLACION HIJOS SIN ELITE')
for i in range (len(hijos)):
    print(hijos[i])

print('\nPOBLACION HIJOS ELITE')
for i in range (len(hijos_elite)):
    print(hijos_elite[i])

print('\nPOBLACION HIJOS SELECCION RANGO')
for i in range (len(hijos_rango)):
    print(hijos_rango[i])'''
