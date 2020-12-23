from listaDoble import *
from TablasD import *

Ld = ListaDOBLE()
T = TablasArboles(Ld)

def createDatabase(database : str)-> int:
    res_1 = Ld.agregarLista(database)
    return res_1
def showDatabases() -> list:
    res_2 = Ld.imprimir()
    return res_2
def alterDatabase(databaseOld, databaseNew) -> int:
    res_3 = Ld.modificarNodo(databaseOld,databaseNew)
    return res_3
def dropDatabase(database: str) -> int:
    res_4 = Ld.eliminarNodo(database)
    return res_4
def grafica():
    #gra = Ld.GraficarConArchivo()
    pass


#Tablas

def createTable(database,table,numberColumns) :
    return T.createT(database,table,numberColumns)
def showTables(database) :
    return T.showT(database)
def extractTable(self, database, table) :
    return T.extractT(database, table)
def extractRangeTable(self, database, table, columnNumber, lower, upper) :
    return T.extractRT(database, table, columnNumber, lower, upper)

#entran las funciones 5-10 de Edgar

def alterAddColumn(self, database, table, default) :
    return T.alterAC(database, table, default)
def alterTable(database,tableOld,tableNew) :
    return T.alterT(database,tableOld,tableNew)
def alterDropColumn(database, table, columnNumber) :
    return T.alterDC(database, table, columnNumber)
def dropTable(database,table) :
    return T.dropT(database,table)