# import avl
# import b
# import bplus
import DictMode.DictMode as DM
# import isam
# import json
# import hash

currentMode = ""
# ----------Bases de datos------------------
def createDatabase(database, mode, encoding):
    try:
        if not isValidMode(mode):
            return 3
        elif not isValidEncoding(encoding):
            return 4
        else:    
            currentMode = mode
            #llamar encoding
            r = chooseMode(mode,database)
            return r
    except:
        return 1
    
def alterDatabaseMode(database, mode):
    pass

def showDatabases():
    if currentMode == 'avl':
        pass
        # return avl.showDatabases()
    elif currentMode == 'b':
        pass
        # return b.showDatabases()
    elif currentMode == 'bplus':
        pass
        # return bplus.showDatabases()
    elif currentMode == 'dict':
        pass
        # return DictMode.showDatabases()
    elif currentMode == 'isam':
        pass
        # return isam.showDatabases()
    elif currentMode == 'json':
        pass
        # return json.showDatabases()
    elif currentMode == 'hash':
        pass
        # return hash.showDatabases()

def alterDatabase(old, new):
    if currentMode == 'avl':
        pass
        # return avl.alterDatabase(old, new)
    elif currentMode == 'b':
        pass
        # return b.alterDatabase(old, new)
    elif currentMode == 'bplus':
        pass
        # return bplus.alterDatabase(old, new)
    elif currentMode == 'dict':
        pass
        # return DictMode.alterDatabase(old, new)
    elif currentMode == 'isam':
        pass
        # return isam.alterDatabase(old, new)
    elif currentMode == 'json':
        pass
        # return json.alterDatabase(old, new)
    elif currentMode == 'hash':
        pass
        # return hash.alterDatabase(old, new)

def dropDatabase(database):
    if currentMode == 'avl':
        pass
        # return avl.dropDatabase(database)
    elif currentMode == 'b':
        pass
        # return b.dropDatabase(database)
    elif currentMode == 'bplus':
        pass
        # return bplus.dropDatabase(database)
    elif currentMode == 'dict':
        pass
        # return DictMode.dropDatabase(database)
    elif currentMode == 'isam':
        pass
        # return isam.dropDatabase(database)
    elif currentMode == 'json':
        pass
        # return json.dropDatabase(database)
    elif currentMode == 'hash':
        pass
        # return hash.dropDatabase(database)

#-------------TABLAS-------------------
def createTable(database, table, numbercolumns):
    if currentMode == 'avl':
        pass
        # return avl.createTable(database, table, numbercolumns)
    elif currentMode == 'b':
        pass
        # return b.createTable(database, table, numbercolumns)
    elif currentMode == 'bplus':
        pass
        # return bplus.createTable(database, table, numbercolumns)
    elif currentMode == 'dict':
        pass
        # return DictMode.createTable(database, table, numbercolumns)
    elif currentMode == 'isam':
        pass
        # return isam.createTable(database, table, numbercolumns)
    elif currentMode == 'json':
        pass
        # return json.createTable(database, table, numbercolumns)
    elif currentMode == 'hash':
        pass
        # return hash.createTable(database, table, numbercolumns)

def alterTableMode(database, table, mode):
    pass
def alterTableAddFK(database: str, table: str, indexName: str, columns: list,  tableRef: str, columnsRef: list):
    pass
def alterTableDropFK(database: str, table: str, indexName: str) -> int:
    pass

def alterTable(database, tableOld, tableNew):
    if currentMode == 'avl':
        pass
        # return avl.alterTable(database, tableOld, tableNew)
    elif currentMode == 'b':
        pass
        # return b.alterTable(database, tableOld, tableNew)
    elif currentMode == 'bplus':
        pass
        # return bplus.alterTable(database, tableOld, tableNew)
    elif currentMode == 'dict':
        pass
        # return DictMode.alterTable(database, tableOld, tableNew)
    elif currentMode == 'isam':
        pass
        # return isam.alterTable(database, tableOld, tableNew)
    elif currentMode == 'json':
        pass
        # return json.alterTable(database, tableOld, tableNew)
    elif currentMode == 'hash':
        pass
        # return hash.alterTable(database, tableOld, tableNew)

def dropTable(database, table):
    if currentMode == 'avl':
        pass
        # return avl.dropTable(database, table)
    elif currentMode == 'b':
        pass
        # return b.dropTable(database, table)
    elif currentMode == 'bplus':
        pass
        # return bplus.dropTable(database, table)
    elif currentMode == 'dict':
        pass
        # return DictMode.dropTable(database, table)
    elif currentMode == 'isam':
        pass
        # return isam.dropTable(database, table)
    elif currentMode == 'json':
        pass
        # return json.dropTable(database, table)
    elif currentMode == 'hash':
        pass
        # return hash.dropTable(database, table)

def showTables(database):
    if currentMode == 'avl':
        pass
        # return avl.showTables(database)
    elif currentMode == 'b':
        pass
        # return b.showTables(database)
    elif currentMode == 'bplus':
        pass
        # return bplus.showTables(database)
    elif currentMode == 'dict':
        pass
        # return DictMode.showTables(database)
    elif currentMode == 'isam':
        pass
        # return isam.showTables(database)
    elif currentMode == 'json':
        pass
        # return json.showTables(database)
    elif currentMode == 'hash':
        pass
        # return hash.showTables(database)

#--------Registros----------------------
def alterAddPK(database, table, columns):
    if currentMode == 'avl':
        pass
        # return avl.alterAddPK(database, table, columns)
    elif currentMode == 'b':
        pass
        # return b.alterAddPK(database, table, columns)
    elif currentMode == 'bplus':
        pass
        # return bplus.alterAddPK(database, table, columns)
    elif currentMode == 'dict':
        pass
        # return DictMode.alterAddPK(database, table, columns)
    elif currentMode == 'isam':
        pass
        # return isam.alterAddPK(database, table, columns)
    elif currentMode == 'json':
        pass
        # return json.alterAddPK(database, table, columns)
    elif currentMode == 'hash':
        pass
        # return hash.alterAddPK(database, table, columns)

def alterDropPK(database, table):
    if currentMode == 'avl':
        pass
        # return avl.alterDropPK(database, table)
    elif currentMode == 'b':
        pass
        # return b.alterDropPK(database, table)
    elif currentMode == 'bplus':
        pass
        # return bplus.alterDropPK(database, table)
    elif currentMode == 'dict':
        pass
        # return DictMode.alterDropPK(database, table)
    elif currentMode == 'isam':
        pass
        # return isam.alterDropPK(database, table)
    elif currentMode == 'json':
        pass
        # return json.alterDropPK(database, table)
    elif currentMode == 'hash':
        pass
        # return hash.alterDropPK(database, table)

def insert(database, table, register):
    if currentMode == 'avl':
        pass
        # return avl.insert(database, table, register)
    elif currentMode == 'b':
        pass
        # return b.insert(database, table, register)
    elif currentMode == 'bplus':
        pass
        # return bplus.insert(database, table, register)
    elif currentMode == 'dict':
        pass
        # return DictMode.insert(database, table, register)
    elif currentMode == 'isam':
        pass
        # return isam.insert(database, table, register)
    elif currentMode == 'json':
        pass
        # return json.insert(database, table, register)
    elif currentMode == 'hash':
        pass
        # return hash.insert(database, table, register)

def update(database, table, register, columns):
    if currentMode == 'avl':
        pass
        # return avl.update(database, table, register, columns)
    elif currentMode == 'b':
        pass
        # return b.update(database, table, register, columns)
    elif currentMode == 'bplus':
        pass
        # return bplus.update(database, table, register, columns)
    elif currentMode == 'dict':
        pass
        # return DictMode.update(database, table, register, columns)
    elif currentMode == 'isam':
        pass
        # return isam.update(database, table, register, columns)
    elif currentMode == 'json':
        pass
        # return json.update(database, table, register, columns)
    elif currentMode == 'hash':
        pass
        # return hash.update(database, table, register, columns)

def delete(database, table, columns):
    if currentMode == 'avl':
        pass
        # return avl.delete(database, table, columns)
    elif currentMode == 'b':
        pass
        # return b.delete(database, table, columns)
    elif currentMode == 'bplus':
        pass
        # return bplus.delete(database, table, columns)
    elif currentMode == 'dict':
        pass
        # return DictMode.delete(database, table, columns)
    elif currentMode == 'isam':
        pass
        # return isam.delete(database, table, columns)
    elif currentMode == 'json':
        pass
        # return json.delete(database, table, columns)
    elif currentMode == 'hash':
        pass
        # return hash.delete(database, table, columns)

def truncate(database, table):
    if currentMode == 'avl':
        pass
        # return avl.truncate(database, table)
    elif currentMode == 'b':
        pass
        # return b.truncate(database, table)
    elif currentMode == 'bplus':
        pass
        # return bplus.truncate(database, table)
    elif currentMode == 'dict':
        pass
        # return DictMode.truncate(database, table)
    elif currentMode == 'isam':
        pass
        # return isam.truncate(database, table)
    elif currentMode == 'json':
        pass
        # return json.truncate(database, table)
    elif currentMode == 'hash':
        pass
        # return hash.truncate(database, table)

def alterAddColumn(database,table, default):
    if currentMode == 'avl':
        pass
        # return avl.alterAddColumn(database,table, default)
    elif currentMode == 'b':
        pass
        # return b.alterAddColumn(database,table, default)
    elif currentMode == 'bplus':
        pass
        # return bplus.alterAddColumn(database,table, default)
    elif currentMode == 'dict':
        pass
        # return DictMode.alterAddColumn(database,table, default)
    elif currentMode == 'isam':
        pass
        # return isam.alterAddColumn(database,table, default)
    elif currentMode == 'json':
        pass
        # return json.alterAddColumn(database,table, default)
    elif currentMode == 'hash':
        pass
        # return hash.alterAddColumn(database,table, default)

def alterDropColumn(database, table, columnNumber):
    if currentMode == 'avl':
        pass
        # return avl.alterDropColumn(database, table, columnNumber)
    elif currentMode == 'b':
        pass
        # return b.alterDropColumn(database, table, columnNumber)
    elif currentMode == 'bplus':
        pass
        # return bplus.alterDropColumn(database, table, columnNumber)
    elif currentMode == 'dict':
        pass
        # return DictMode.alterDropColumn(database, table, columnNumber)
    elif currentMode == 'isam':
        pass
        # return isam.alterDropColumn(database, table, columnNumber)
    elif currentMode == 'json':
        pass
        # return json.alterDropColumn(database, table, columnNumber)
    elif currentMode == 'hash':
        pass
        # return hash.alterDropColumn(database, table, columnNumber)

def extractTable(database, table):
    if currentMode == 'avl':
        pass
        # return avl.extractTable(database, table)
    elif currentMode == 'b':
        pass
        # return b.extractTable(database, table)
    elif currentMode == 'bplus':
        pass
        # return bplus.extractTable(database, table)
    elif currentMode == 'dict':
        pass
        # return DictMode.extractTable(database, table)
    elif currentMode == 'isam':
        pass
        # return isam.extractTable(database, table)
    elif currentMode == 'json':
        pass
        # return json.extractTable(database, table)
    elif currentMode == 'hash':
        pass
        # return hash.extractTable(database, table)

def extractRow(database, table, columns):
    if currentMode == 'avl':
        pass
        # return avl.extractRow(database, table, columns)
    elif currentMode == 'b':
        pass
        # return b.extractRow(database, table, columns)
    elif currentMode == 'bplus':
        pass
        # return bplus.extractRow(database, table, columns)
    elif currentMode == 'dict':
        pass
        # return DictMode.extractRow(database, table, columns)
    elif currentMode == 'isam':
        pass
        # return isam.extractRow(database, table, columns)
    elif currentMode == 'json':
        pass
        # return json.extractRow(database, table, columns)
    elif currentMode == 'hash':
        pass
        # return hash.extractRow(database, table, columns)

def loadCSV(file,database,table):
    if currentMode == 'avl':
        pass
        # return avl.loadCSV(file,database,table)
    elif currentMode == 'b':
        pass
        # return b.loadCSV(file,database,table)
    elif currentMode == 'bplus':
        pass
        # return bplus.loadCSV(file,database,table)
    elif currentMode == 'dict':
        pass
        # return DictMode.loadCSV(file,database,table)
    elif currentMode == 'isam':
        pass
        # return isam.loadCSV(file,database,table)
    elif currentMode == 'json':
        pass
        # return json.loadCSV(file,database,table)
    elif currentMode == 'hash':
        pass
        # return hash.loadCSV(file,database,table)

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
        pass
        # return avl.createDatabase(database)
    elif mode == 'b':
        pass
        # return b.createDatabase(database)
    elif mode == 'bplus':
        pass
        # return bplus.createDatabase(database)
    elif mode == 'dict':
        #DM.createDatabase(database)
        #DM.DictMode.bd.createDatabase(database)
        
        r = DM.createDatabase(database)
        return r
    elif mode == 'isam':
        pass
        # return isam.createDatabase(database)
    elif mode == 'json':
        pass8
        # return json.createDatabase(database)
    elif mode == 'hash':
        pass
        # return hash.createDatabase(database)

print(createDatabase("miBase","dict","utf8"))

#print(DM.createDatabase("base1"))
