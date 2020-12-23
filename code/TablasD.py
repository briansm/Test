
from listaDTablas import *

class TablasArboles:  
    def __init__(self,bd) :
        self.bd=bd
        
    def agregarColumna(self,val) :
        for i in range(len(ab.listRegister)) :
            ab.listRegister[i].register.append(val)
        return True
        #descomentar para confirmar
        #print(ab.listRegister[0].register)

    def eliminarColumna(self,num) :
        for i in range(len(ab.listRegister)):
            del ab.listRegister[i].register[num]
        return True
        #descomentar para confirmar
        #print(ab.listRegister[0].register)
  
        

#Funcion 1 - crear tabla
# def createTable(database: str, table: str, numberColumns: int) -> int:    
    def createT(self,database,table,numberColumns) :
        #print(e)
        
        bdEncontrada=self.bd.buscarNodo(database)
        if bdEncontrada != None and bdEncontrada != 0:      #se agrego la 2da condicion por si retorna algun numero                                       
            if bdEncontrada.tablas == None :
                bdEncontrada.tablas = ListaDobledeArboles()
            if bdEncontrada.tablas.buscar(table) == False :
                #BD encontrada.tablas=table
                bdEncontrada.tablas.insertar(table,numberColumns)
                if bdEncontrada.tablas != None :
                    #return ("Operacion exitosa")
                    return (0)
                else:
                    #return ("Error en la operacion")
                    return (1)
            else:
                #return ("Tabla existente")
                return (3)
        else:                                                                      
            #return ("BD inexistente")
            return (2)                                                             

#Funcion 2 - mostrar tablas
# def showTables(database: str) -> list:                    
    def showT(self,database) :
        #tablas = []
        bdEncontrada=self.bd.buscarNodo(database)
        if bdEncontrada != None and bdEncontrada != 0 : 
            return bdEncontrada.tablas.verNodos()
        else:                                                                    
            return None                                                         

#Funcion 3 - mostrar el contenido de la tabla
# def extractTable(database: str, table: str) -> list:
    def extractT(self, database, table) :
        list = []
        bdEncontrada=self.bd.buscarNodo(database)
        if bdEncontrada != None and bdEncontrada != 0 :                                            
            if bdEncontrada.tablas.buscar(table) == True :
                for i in range(len(ab.listRegister)):
                    list.append(ab.listRegister[i].register)
                    #para confirmar
                    #print(p.extractTable("bd1","tabla1"))
                    #print(objetoClaseTabla.extractTable("Nombre de la base de datos","Nombre de la tabla"))
                return list            
            else:
                #return("tableNew existente")
                return None
        else:                                                                     
            #return ("BD inexistente")
            return None 

#Funcion 4 - muestra un determinado numero de elementos de la tabla
# def extractRangeTable(database: str, table: str, columnNumber: int, lower: any, upper: any) -> list:
    def extractRT(self, database, table, columnNumber, lower, upper) :
        list = []
        bdEncontrada=self.bd.buscarNodo(database)
        if bdEncontrada != None and bdEncontrada != 0 :                                            
            if bdEncontrada.tablas.buscar(table) == True :
                for i in range(len(ab.listRegister)):
                    if str(lower) <= ab.listRegister[i].register[int(columnNumber)] and ab.listRegister[i].register[int(columnNumber)] <= str(upper) :
                        list.append(ab.listRegister[i].register[columnNumber])
                return list  
            else:
                #return("tableNew existente")
                return None
        else:                                                                     
            #return ("BD inexistente")
            return None 

#Funcion 9 - cambiar nombre a la tabla
# def alterTable(database: str, tableOld: str, tableNew: str) -> int:  
    def alterT(self,database,tableOld,tableNew) :
        bdEncontrada=self.bd.buscarNodo(database)
        if bdEncontrada != None and bdEncontrada != 0 :                                            
            if bdEncontrada.tablas.buscar(tableNew) == False :
                if bdEncontrada.tablas.buscar(tableOld) == True :
                    r = bdEncontrada.tablas.modificar(tableOld,tableNew)
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
        else:                                                                     
            #return ("BD inexistente")
            return (2)                                                            

#Funcion 10 - agregar columna
# def alterAddColumn(database: str, table: str, default: any) -> int:
    def alterAC(self, database, table, default) :
        bdEncontrada=self.bd.buscarNodo(database)
        if bdEncontrada != None and bdEncontrada != 0 :
            if bdEncontrada.tablas.buscar(table) == True :
                if self.agregarColumna(default) == True :
                    #return ("Operacion exitosa")
                    return 0
                else:
                    #return ("Error en la operacion")
                    return (1)
            else:
                #return ("Tabla inexistente")
                return (3)
        else:                                                                   
            #return ("BD inexistente")
            return (2)

#Funcion 11 - eliminar columna
# def alterDropColumn(database: str, table: str, columnNumber: int) -> int:
    def alterDC(self, database, table, columnNumber) :
        bdEncontrada=self.bd.buscarNodo(database)
        if bdEncontrada != None and bdEncontrada != 0 :
            if bdEncontrada.tablas.buscar(table) == True :
                if self.eliminarColumna(columnNumber) == True :
                    #return ("Operacion exitosa")
                    return 0
                else:
                    #return ("Error en la operacion")
                    return (1)
            else:
                #return ("Tabla inexistente")
                return (3)
        else:                                                                   
            #return ("BD inexistente")
            return (2) 
            
#Funcion 12 - eliminar tabla
# def dropTable(database: str, table: str) -> int:           
    def dropT(self,database,table) :
        bdEncontrada=self.bd.buscarNodo(database)
        if bdEncontrada != None and bdEncontrada != 0 :
            if bdEncontrada.tablas.buscar(table) == True :
                r = bdEncontrada.tablas.eliminar(table)
                if r==0 :
                    #return ("Operacion exitosa")
                    return (0)
                else:
                    #return ("Error en la operacion")
                    return (1)
            else:
                #return ("Tabla inexistente")
                return (3) 
        else:                                                                    
            #return ("BD inexistente")
            return (2) 