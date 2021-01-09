'''
8. Grafos
El storageManager debe tener un paquete de generación de diagramas de estructuras de datos basado en GraphViz.
Para esto se deben crear los siguientes grafos de dependencias:

diagrama de estructura de datos: para mayor detalle ver este enlace.
diagrama de dependencias: este grafo muestra las dependencias funcionales que existen en una tabla específica.
El resultado será gráfico, sin embargo se deben crear dos funciones para generar dichos diagramas.

def graphDSD(database: str) -> str:
Genera un gráfico mediante Graphviz acerca de la base de datos especificada. (UPDATE)
Parámetro database: es el nombre de la base de datos a utilizar.
Valor de retorno: archivo en formato Graphviz para dibujar, None si hay un error.

def graphDF(database: str, table: str) -> str:
Genera un gráfico mediante Graphviz acerca de las dependencias funcionales de una tabla especificada de una base de datos. (UPDATE)
Parámetro database: es el nombre de la base de datos a utilizar.
Parámetro table: es el nombre de la tabla a utilizar.
Valor de retorno: archivo en formato Graphviz para dibujar, None si hay un error.
'''
# ------------------ 8. Grafos ------------------

#def graphDSD(database: str) -> str:
#Relacion de tablas con respecto a las FK
def graphDSD(database: str) :
    if DM.existDB(database) != None :
        GDSD(database)
    else:
        #BD no existe #modificar el numero si es necesario, no recuerdo que devolvia si no la encontraba
        return 1

def GDSD(baseDatos) :

#def graphDF(database: str, table: str) -> str:
#Relacion de registros de 1 tabla con repecto a la PK e indices unicos
def graphDF(database: str, table: str) :
    #if DM.existDB(database) != None :
        #if DM.existTable(table) != None :
            l=[] 
            l.append(extractTable(database,table))
            GDF(table,l)
        #else:
            #tabla inexistente #modificar el numero si es necesario, no recuerdo que devolvia si no la encontraba
            #return 1
    #else:
        #BD inexistente #modificar el numero si es necesario, no recuerdo que devolvia si no la encontraba
        #return 1

def GDF(tabla, lista:list) :
    f = open("Grafo.dot","w")
    f.write("digraph g {\n")
    f.write("node [shape=record]\n")
    f.write("subgraph cluster_0 {")
    f.write("\""+str(lista[0][0][0])+"\";\n")
    for i in range(len(lista[0][0][0])):
        f.write("\""+str(lista[0][i+1][0])+"\";\n") 
    f.write("label=\""+tabla+"\";")
    f.write("color=blue;\n")
    f.write("}")
    for i in range(len(lista[0][0][0])):
        f.write(lista[0][0][0]+"->"+lista[0][i+1][0]+"\n")
    f.write("}")
    f.close()
    os.system("dot -Tjpg Grafo.dot -o Grafo.png")

    #modos iniciales




def v(database,table):
    
    #devuelve el nombre de la bd en esa posicion
    #print(avl.TBL.dbs[0])
    #devuelve el nombre de la tabla de la bd donde se encuentra
    
    l=[] 
    l.append(extractTable(database,table))
    print(l[0][0][0],l[0][1][0])
    vv(table,l)
def vv(tabla,lista:list):
    #con los modos "hash" y "b" detecta dos veces un registro
    # se uso de prueba t1x'n' y era el valor 1 el duplicado, no paso con ningun otro modo
    f = open("Grafo.dot","w")
    f.write("digraph g {\n")
    f.write("node [shape=record]\n")
    f.write("subgraph cluster_0 {")
    f.write("\""+str(lista[0][0][0])+"\";\n")
    for i in range(len(lista[0][0][0])):
        f.write("\""+str(lista[0][i+1][0])+"\";\n") 
    f.write("label=\""+tabla+"\";")
    f.write("color=blue;\n")
    f.write("}")
    for i in range(len(lista[0][0][0])):
        f.write(lista[0][0][0]+"->"+lista[0][i+1][0]+"\n")
    f.write("}")
    f.close()
    os.system("dot -Tjpg Grafo.dot -o Grafo.png")