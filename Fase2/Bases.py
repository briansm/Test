from storage.avl import avlMode as avl
from storage.b import BMode as b
from storage.bplus import BPlusMode as bplus
from storage.DictMode import DictMode as DM
from storage.isam import ISAMMode as isam
from storage.json import jsonMode as j
#from storage.Hash import HashMode as Hash
import hashlib
from storage.HashWindows import HashMode as Hash
import os
currentMode,avlList,bList,bplusList,dictList,jsonList,isamList,hashList = [],[],[],[],[],[],[],[]

global lista
lista = list()

class controlFK:
    def __init__(self, database, table, indexName, columns, tableRef, columnsRef):
        self.database = database
        self.table = table
        self.indexName = indexName
        self.columns = columns
        self.tableRef = tableRef
        self.columnsRef = columnsRef


# ----------Bases de datos------------------
def createDatabase(database, mode, encoding):
    try:
        if not isValidMode(mode):
            return 3
        elif not isValidEncoding(encoding):
            return 4
        else:    
            currentMode.append(mode)
            #llamar encoding
            return chooseMode(mode,database)
    except:
        return 1
    
def alterDatabaseMode(database, mode):
    pass

def showDatabases():
    showAvl = avl.showDatabases()
    showB = b.showDatabases()
    showBP = bplus.showDatabases()
    showDict = DM.showDatabases()
    showIsam = isam.showDatabases()
    showHash = Hash.showDatabases()
    showJson = j.showDatabases()
    showALL = 'avl = ' + str(showAvl)+'\n'+'b = ' + str(showB)+'\n'+'bplus = ' + str(showBP)+'\n'+'dict = ' + str(showDict)+'\n'+'isam = ' + str(showIsam)+'\n'+'json = ' + str(showJson) +'\n'+'hash = ' + str(showHash)
                
    return showALL

def alterDatabase(old, new):
    if searchInMode(old) != None:
        currentMode = searchInMode(old)
        if currentMode == 'avl':
            avlList.append(new)
            return avl.alterDatabase(old, new)
        elif currentMode == 'b':
            bList.append(new)
            return b.alterDatabase(old, new)
        elif currentMode == 'bplus':
            bplusList.append(new)
            return bplus.alterDatabase(old, new)
        elif currentMode == 'dict':
            dictList.append(new)
            return DM.alterDatabase(old, new)
        elif currentMode == 'isam':
            isamList.append(new)
            return isam.alterDatabase(old, new)
        elif currentMode == 'json':
            jsonList.append(new)
            return j.alterDatabase(old, new)
        elif currentMode == 'hash':
            hashList.append(new)
            return Hash.alterDatabase(old, new)
        
def dropDatabase(database):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            return avl.dropDatabase(database)
        elif currentMode == 'b':
            return b.dropDatabase(database)
        elif currentMode == 'bplus':
            return bplus.dropDatabase(database)
        elif currentMode == 'dict':
            return DM.dropDatabase(database)
        elif currentMode == 'isam':
            return isam.dropDatabase(database)
        elif currentMode == 'json':
            return j.dropDatabase(database)
        elif currentMode == 'hash':
            return Hash.dropDatabase(database)
    else:
        return 2

#-------------TABLAS-------------------
def createTable(database, table, numbercolumns):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            avlList.append(table)
            return avl.createTable(database, table, numbercolumns)
        elif currentMode == 'b':
            bList.append(table)
            return b.createTable(database, table, numbercolumns)
        elif currentMode == 'bplus':
            bplusList.append(table)
            return bplus.createTable(database, table, numbercolumns)
        elif currentMode == 'dict':
            dictList.append(table)
            return DM.createTable(database, table, numbercolumns)
        elif currentMode == 'isam':
            isamList.append(table)
            return isam.createTable(database, table, numbercolumns)
        elif currentMode == 'json':
            jsonList.append(table)
            return j.createTable(database, table, numbercolumns)
        elif currentMode == 'hash':
            hashList.append(table)
            return Hash.createTable(database, table, numbercolumns)
    else:
        return 2

def alterTableMode(database, table, mode):
    pass
def alterTableAddFK(database, table, indexName, columns,  tableRef, columnsRef):
    
    try:    
        Temporal = showTables(database)
        bandera = False
        contador = 0
    except:
        return 2

    try: 
        for i in Temporal:
            if table == i:
                contador += 1
                if contador >= 1:
                    bandera = True
                

        if len(columns) <= 0 or len(columnsRef) <=0 or len(columns) != len(columnsRef):
            return 4

        elif bandera == False:
            return 3

        else:
            lista.append(controlFK(database,table,indexName,columns,tableRef,columnsRef))
            return 0
    except:
        return 1

def alterTableDropFK(database, table, indexName):
    try:
        for j in range(len(lista)):
            if database == lista[j].database:
                for k in range(len(lista)):
                    if table == lista[k].table:
                        for i in range(len(lista)):
                            if indexName == lista[i].indexName:
                                lista.pop(i)
                                return 0
                            else:
                                return 4
                    else:
                        return 3
            else:
                return 2
    except:
        return 1

def alterTable(database, tableOld, tableNew):
    if searchInMode(tableOld) != None:
        currentMode = searchInMode(tableOld)
        if currentMode == 'avl':
            avlList.append(tableNew)
            return avl.alterTable(database, tableOld, tableNew)
        elif currentMode == 'b':
            bList.append(tableNew)
            return b.alterTable(database, tableOld, tableNew)
        elif currentMode == 'bplus':
            bplusList.append(tableNew)
            return bplus.alterTable(database, tableOld, tableNew)
        elif currentMode == 'dict':
            dictList.append(tableNew)
            return DM.alterTable(database, tableOld, tableNew)
        elif currentMode == 'isam':
            isamList.append(tableNew)
            return isam.alterTable(database, tableOld, tableNew)
        elif currentMode == 'json':
            jsonList.append(tableNew)
            return j.alterTable(database, tableOld, tableNew)
        elif currentMode == 'hash':
            hashList.append(tableNew)
            return Hash.alterTable(database, tableOld, tableNew)
    else:
        return 2

def dropTable(database, table):
    if searchInMode(table) != None:
        currentMode = searchInMode(table)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.dropTable(database, table)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.dropTable(database, table)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.dropTable(database, table)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.dropTable(database, table)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.dropTable(database, table)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.dropTable(database, table)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.dropTable(database, table)
    else:
        return 2

def showTables(database):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.showTables(database)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.showTables(database)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.showTables(database)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.showTables(database)
        elif currentMode == 'isam':
            # isamList.append(database)
            return isam.showTables(database)
        elif currentMode == 'json':
            # jsonList.append(database)
            return j.showTables(database)
        elif currentMode == 'hash':
            # hashList.append(database)
            return Hash.showTables(database)
    else:
        return 2

#--------Registros----------------------
def alterAddPK(database, table, columns):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.alterAddPK(database, table, columns)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.alterAddPK(database, table, columns)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.alterAddPK(database, table, columns)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.alterAddPK(database, table, columns)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.alterAddPK(database, table, columns)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.alterAddPK(database, table, columns)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.alterAddPK(database, table, columns)
    else:
        return 2

def alterDropPK(database, table):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.alterDropPK(database, table)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.alterDropPK(database, table)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.alterDropPK(database, table)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.alterDropPK(database, table)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.alterDropPK(database, table)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.alterDropPK(database, table)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.alterDropPK(database, table)
    else:
        return 2

def insert(database, table, register):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.insert(database, table, register)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.insert(database, table, register)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.insert(database, table, register)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.insert(database, table, register)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.insert(database, table, register)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.insert(database, table, register)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.insert(database, table, register)
    else:
        return 2

def update(database, table, register, columns):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.update(database, table, register, columns)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.update(database, table, register, columns)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.update(database, table, register, columns)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.update(database, table, register, columns)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.update(database, table, register, columns)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.update(database, table, register, columns)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.update(database, table, register, columns)
    else:
        return 2

def delete(database, table, columns):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.delete(database, table, columns)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.delete(database, table, columns)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.delete(database, table, columns)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.delete(database, table, columns)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.delete(database, table, columns)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.delete(database, table, columns)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.delete(database, table, columns)
    else:
        return 2

def truncate(database, table):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.truncate(database, table)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.truncate(database, table)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.truncate(database, table)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.truncate(database, table)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.truncate(database, table)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.truncate(database, table)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.truncate(database, table)
    else:
        return 2

def alterAddColumn(database,table, default):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.alterAddColumn(database,table, default)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.alterAddColumn(database,table, default)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.alterAddColumn(database,table, default)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.alterAddColumn(database,table, default)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.alterAddColumn(database,table, default)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.alterAddColumn(database,table, default)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.alterAddColumn(database,table, default)
    else:
        return 2

def alterDropColumn(database, table, columnNumber):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.alterDropColumn(database, table, columnNumber)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.alterDropColumn(database, table, columnNumber)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.alterDropColumn(database, table, columnNumber)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.alterDropColumn(database, table, columnNumber)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.alterDropColumn(database, table, columnNumber)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.alterDropColumn(database, table, columnNumber)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.alterDropColumn(database, table, columnNumber)
    else:
        return 2

def extractTable(database, table):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.extractTable(database, table)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.extractTable(database, table)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.extractTable(database, table)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.extractTable(database, table)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.extractTable(database, table)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.extractTable(database, table)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.extractTable(database, table)
    else:
        return 2

def extractRangeTable(database, table, columnNumber, lower, upper):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.extractRangeTable(database, table, columnNumber, lower, upper)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.extractRangeTable(database, table, columnNumber, lower, upper)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.extractRangeTable(database, table, columnNumber, lower, upper)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.extractRangeTable(database, table, columnNumber, lower, upper)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.extractRangeTable(database, table, columnNumber, lower, upper)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.extractRangeTable(database, table, lower, upper)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.extractRangeTable(database, table, columnNumber, lower, upper)
    else:
        return 2

def extractRow(database, table, columns):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.extractRow(database, table, columns)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.extractRow(database, table, columns)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.extractRow(database, table, columns)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.extractRow(database, table, columns)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.extractRow(database, table, columns)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.extractRow(database, table, columns)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.extractRow(database, table, columns)
    else:
        return 2

def loadCSV(file,database,table):
    if searchInMode(database) != None:
        currentMode = searchInMode(database)
        if currentMode == 'avl':
            # avlList.append(tableNew)
            return avl.loadCSV(file,database,table)
        elif currentMode == 'b':
            # bList.append(tableNew)
            return b.loadCSV(file,database,table)
        elif currentMode == 'bplus':
            # bplusList.append(tableNew)
            return bplus.loadCSV(file,database,table)
        elif currentMode == 'dict':
            # dictList.append(tableNew)
            return DM.loadCSV(file,database,table)
        elif currentMode == 'isam':
            # isamList.append(tableNew)
            return isam.loadCSV(file,database,table)
        elif currentMode == 'json':
            # jsonList.append(tableNew)
            return j.loadCSV(file,database,table)
        elif currentMode == 'hash':
            # hashList.append(tableNew)
            return Hash.loadCSV(file,database,table)
    else:
        return 2

def checksumDatabase(database, mode):
    MegaCadena = ""

    try:
        lista = showTables(database)
        MegaCadena = MegaCadena + database

        for i in lista:
            MegaCadena = MegaCadena + i

            for j in extractTable(database, i):
                MegaCadena = MegaCadena + str(j)
        if mode == "MD5":
            return CodMD5(MegaCadena)
        else:
            return CodSHA256(MegaCadena)
    
    except:
        return None

def checksumTable(database, table, mode):
    MegaCadena = ""

    try:
        lista = showTables(database)

        for i in lista:
            if i == table:
                MegaCadena = MegaCadena + i
            
            for j in extractTable(database, i):
                if i == table:
                    MegaCadena = MegaCadena + str(j)

        
        if mode == "MD5":
            return CodMD5(MegaCadena)
        else:
            return CodSHA256(MegaCadena)

    except:
        return None

def CodMD5(Entrada):
    MD5Codigo = hashlib.md5()
    MD5Codigo.update(Entrada.encode('utf8'))
    Proceso = MD5Codigo.hexdigest()
    return Proceso

def CodSHA256(Entrada):
    SHACodigo = hashlib.sha256()
    SHACodigo.update(Entrada.encode('utf8'))
    Proceso = SHACodigo.hexdigest()
    return Proceso


#----------------------------------------------------
def isValidMode(mode):
    listMode = ['avl', 'b', 'bplus', 'dict', 'isam', 'json', 'hash']
    for check in listMode:
        if check == mode:
            return True
    return False

def isValidEncoding(encoding):
    listEncoding = ['ascii', 'iso-8859-1', 'utf8']
    for check in listEncoding:
        if check == encoding:
            return True
    return False

def chooseMode(mode,database):
    if mode == 'avl':
        if avl.createDatabase(database) == 0:
            avlList.append(database)
            return 0
        else:
            return avl.createDatabase(database)
    elif mode == 'b':
        if b.createDatabase(database) == 0:
            bList.append(database)
            return 0
        else:
            return b.createDatabase(database)
    elif mode == 'bplus':
        if bplus.createDatabase(database) == 0:
            bplusList.append(database)
            return 0
        else:
            return bplus.createDatabase(database)
    elif mode == 'dict':
        if DM.createDatabase(database) == 0:
            dictList.append(database)
            return 0
        else:
            return DM.createDatabase(database)
    elif mode == 'isam':
        if isam.createDatabase(database) == 0:
            isamList.append(database)
            return 0
        else:
            return isam.createDatabase(database)
    elif mode == 'json':
        if j.createDatabase(database) == 0:
            jsonList.append(database)
            return 0
        else:
            return j.createDatabase(database)
    elif mode == 'hash':
        if Hash.createDatabase(database) == 0:
            hashList.append(database)
            return 0
        else:
            return Hash.createDatabase(database)

def searchInMode(value):
    if value in avlList:
        return 'avl'
    elif value in bList:
        return 'b'
    elif value in bplusList:
        return 'bplus'
    elif value in dictList:
        return 'dict'
    elif value in jsonList:
        return 'json'
    elif value in isamList:
        return 'isam'
    elif value in hashList:
        return 'hash'
    else:
        return None

# print(createDatabase('hola','isam','ascii'))
# print(showDatabases())
# print(showTables('calificacion'))

print(createDatabase("Base1","avl","utf8"))   
  

print(createTable('Base1','Pais',4))
print(createTable('Base1','Paises',4))

print(insert('Base1', 'Pais', ['GTM', 'Guatemala',  'Central America', 108889]))
print(insert('Base1', 'Paises', ['SLV', 'El Salvado', 'Central America',  21041]))

# print(showDatabases())
# print(showTables('Base1'))

print(checksumDatabase('Base1','SHA256'))
print(checksumTable('Base1','Pais','MD5'))

print(alterTableAddFK('Base1','Pais','Perritos',['Nombre'],'Paises',['NombreP']))
print(alterTableDropFK('Base1','Pais','Perritos'))


# ------------------ 8. Grafos ------------------

#def graphDSD(database: str) -> str:
#Relacion de tablas con respecto a las FK #no son utiles todavia, al no usar fk no funcionan
def graphDSD(database: str) :
    if DM.existDB(database) != None :
        GDSD(database)
    else:
        #BD no existe #modificar el numero si es necesario, no recuerdo que devolvia si no la encontraba
        return 1

def GDSD(baseDatos) :
    pass
#def graphDF(database: str, table: str) -> str:
#Relacion de registros de 1 tabla con repecto a la PK e indices unicos
def graphDF(database: str, table: str) :
    l=[] 
    l.append(extractTable(database,table))
    GDF(table,l)

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

    