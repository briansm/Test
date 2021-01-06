from listaDoble import *
from TablasD import *

# from BTree import *

# bTree = BTree()
# bTree.columPK = [0]
# bTree.maxColumna = 3  

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
def extractTable(database, table) :
    return T.extractT(database, table)
def extractRangeTable(database, table, columnNumber, lower, upper) :
    return T.extractRT(database, table, columnNumber, lower, upper)

#entran las funciones 5-10 de Edgar

def alterAddColumn( database, table, default) :
    return T.alterAC(database, table, default)
def alterTable(database,tableOld,tableNew) :
    return T.alterT(database,tableOld,tableNew)
def alterDropColumn(database, table, columnNumber) :
    return T.alterDC(database, table, columnNumber)
def dropTable(database,table) :
    return T.dropT(database,table)
    
#-------------Tuplas-------------------

# def loadCSV(filepath, database, table):
#     if Ld.buscarModificar(database) == 2:
#         res_1 = bTree.loadCSV(filepath, database, table)
#         return res_1
#     else:
#         return 2

def insertT(database, table, register) :
    return T.insert(database,table,register)

def loadCSV(filepath, database, table):
    return T.load(filepath, database, table)

def extractRow(database, table, columns):
    return T.extract(database, table, columns)

def update(database, table, register, columns):
    return T.UP(database, table, register, columns)

def graphB(database, table):
    return T.graphbt(database, table)

# def alterAddPk(database,table,columns):
#     return T.alterPK(database,table,columns)

# def extractRow(database, table, columns):
#     res_3 = bTree.extractRow(database, table, columns)
#     return res_3

# def update(database, table, register, columns):
#     res_4 = bTree.update(database, table, register, columns)
#     return res_4

# def graphTree():
#     bTree.graphBTree()
# def delete(parameter_list):
# def truncate():