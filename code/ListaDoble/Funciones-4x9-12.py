#funciones en repositorio de prueba

#import claseBD
#import claseArbolB
import os

class nodo :
    def __init__(self,nombreDeLaTabla,numeroDeColumnasDeLaTabla) :
    #def __init__(self,nombreDeLaTabla,numeroDeColumnasDeLaTabla,listaDeElementosDeLaTabla) : descomentar si es necesario
        self.nombre = nombreDeLaTabla
        self.columnas = numeroDeColumnasDeLaTabla
        #self.elementos = listaDeElementosDeLaTabla
        self.siguiente = None
        self.anterior = None

class ListaDobledeArboles :
    def __init__ (self) :
        self.inicio = None
        self.fin = None

    #Metodo para saber si la lista esta vacia
    def estaVacia(self) :
        return self.inicio is None

    #Metodo para buscar una tabla
    def buscarTabla(self,nombreTabla) :
        aux = self.inicio
        while aux != None :
            if aux.nombre == nombreTabla :
                #print("La tabla existe")
                return True
            aux = aux.siguiente
        #print("La tabla no existe")
        return False

    #Metodo para listar los nodos
    def verNodos(self) :
        aux = self.inicio
        while aux != None :
            print(aux.nombre)
            aux = aux.siguiente

    def insertar(self,nombreTabla,numCol) :
        nuevo = nodo(nombreTabla,numCol)
        # lista vacia
        if self.inicio == None :
            self.inicio=self.fin=nuevo
        else:
            self.fin.siguiente = nuevo
            nuevo.anterior = self.fin
            self.fin = nuevo
        return 0

    def eliminar(self,nombreTabla) :
        pass
        
    def modificar(self,nombreViejo,nombreNuevo):
        aux = self.inicio
        while aux != None :
            if aux.nombre == nombreViejo :
                aux.nombre = nombreNuevo
                return 0
            aux = aux.siguiente


#Funcion 1 - crear tabla
# def createTable(database: str, table: str, numberColumns: int) -> int:     **descomentar lo siguiente al unir el proyecto**
    def createTable(self,database,table,numberColumns) :
        #if buscarBD(database) == True :                                            #esto!
            if self.buscarTabla(table) == False :
                r = self.insertar(table,numberColumns)
                if r==0 :
                    #return ("Operacion exitosa")
                    return (0)
                else:
                    #return ("Error en la operacion")
                    return (1)
            else:
                #return ("Tabla existente")
                return (3)
        #else:                                                                      #esto!
            #return ("BD inexistente")
            #return (2)                                                             #esto!

#Funcion 2 - mostrar tablas
# def showTables(database: str) -> list:                    #**descomentar lo siguiente al unir el proyecto**
    def showTables(self) :
        tablas = []
        #if buscarBD(database) == True :                                            #esto!
        if self.estaVacia() != None :
                #devuelve la lista con los nombres de las tablas
                aux = self.inicio
                while aux != None :
                    tablas.append(aux.nombre)
                    aux = aux.siguiente       
        else:
                return tablas
        #else:                                                                      #esto!
            #return None                                                            #esto!

#Funcion 3 - mostrar el contenido de la tabla
# def extractTable(database: str, table: str) -> list:

#Funcion 4 - muestra un determinado numero de elementos de la tabla
# def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:

#Funcion 9 - cambiar nombre a la tabla
# def alterTable(database: str, tableOld: str, tableNew: str) -> int:  #**descomentar lo siguiente al unir el proyecto**
    def alterTable(self,database,tableOld,tableNew) :
        #if buscarBD(database) == True:                                             #esto!
            if self.buscarTabla(tableNew) == False :
                if self.buscarTabla(tableOld) == True :
                    r = self.modificar(tableOld,tableNew)
                    if r==0 :
                        #return ("Operacion exitosa")
                        return (0)
                    else:
                        #return ("Error en la operacion")
                        return (1)
                else:
                    #return("tableOld no existente")
                    return(3)
            else:
                #return("tableNew existente")
                return(4)
        #else:                                                                      #esto!
            #return ("BD inexistente")
            #return (2)                                                             #esto!


#Funcion 10 - agregar columna
# def alterAddColumn(database: str, table: str, default: any) -> int:

#Funcion 11 - eliminar columna
# def alterDropColumn(database: str, table: str, columnNumber: int) -> int:

#Funcion 12 - eliminar tabla
# def dropTable(database: str, table: str) -> int:                #**descomentar lo siguiente al unir el proyecto**
    def dropTable(self,database,table) :
        #if buscarBD(database) == True :                                            #esto!
            if self.buscarTabla(table) == True :
                r = self.eliminar(table)
                if r==0 :
                    #return ("Operacion exitosa")
                    return (0)
                else:
                    #return ("Error en la operacion")
                    return (1)
            else:
                #return ("Tabla inexistente")
                return (3) 
        #else:                                                                      #esto!
            #return ("BD inexistente")
            #return (2) 


if __name__ == "__main__":
    p = ListaDobledeArboles()
    
    p.createTable("bd1","tabla1",4)
    p.createTable("bd1","tabla2",9)
    p.createTable("bd1","tabla4",6)
    p.createTable("bd1","tabla3",4)
    p.createTable("bd1","tabla9",5)

    #p.verNodos()

    p.showTables()