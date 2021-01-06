import avl.avlMode as avl
import b.BMode as b
import bplus.BPlusMode as bplus
import DictMode.DictMode as DM
# import isam.ISAMMode as isam
# import json.jsonMode as j
# import hash.storage.HashMode as Hash

currentMode,avlList,bList,bplusList,dictList = [],[],[],[],[]

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
    # showIsam = isam.showDatabases()
    # showHash = Hash.showDatabases()
    # showJson = j.showDatabases()
    showALL = 'avl = ' + str(showAvl)+'\n'+'b = ' + str(showB)+'\n'+'bplus = ' + str(showBP)+'\n'+'dict = ' + str(showDict)+'\n'+'isam = ' + ''+'\n'+'json = ' + '' +'\n'+'hash = ' + ''
                
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
            return DictMode.alterDatabase(old, new)
        elif currentMode == 'isam':
            pass
            # isamList.append(new)
            # return isam.alterDatabase(old, new)
        elif currentMode == 'json':
            pass
            # jsonList.append(new)
            # return j.alterDatabase(old, new)
        elif currentMode == 'hash':
            pass
            # hashList.append(new)
            # return Hash.alterDatabase(old, new)
        
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
            return DictMode.dropDatabase(database)
        elif currentMode == 'isam':
            pass
            # return isam.dropDatabase(database)
        elif currentMode == 'json':
            pass
            # return json.dropDatabase(database)
        elif currentMode == 'hash':
            pass
            # return hash.dropDatabase(database)
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
            return DictMode.createTable(database, table, numbercolumns)
        elif currentMode == 'isam':
            pass
            # isamList.append(table)
            # return isam.createTable(database, table, numbercolumns)
        elif currentMode == 'json':
            pass
            # jsonList.append(table)
            # return j.createTable(database, table, numbercolumns)
        elif currentMode == 'hash':
            pass
            # hashList.append(table)
            # return Hash.createTable(database, table, numbercolumns)
    else:
        return 2

def alterTableMode(database, table, mode):
    pass
def alterTableAddFK(database: str, table: str, indexName: str, columns: list,  tableRef: str, columnsRef: list):
    pass
def alterTableDropFK(database: str, table: str, indexName: str) -> int:
    pass

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
            return DictMode.alterTable(database, tableOld, tableNew)
        elif currentMode == 'isam':
            pass
            # isamList.append(tableNew)
            # return isam.alterTable(database, tableOld, tableNew)
        elif currentMode == 'json':
            pass
            # jsonList.append(tableNew)
            # return j.alterTable(database, tableOld, tableNew)
        elif currentMode == 'hash':
            pass
            # hashList.append(tableNew)
            # return Hash.alterTable(database, tableOld, tableNew)
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
            return DictMode.dropTable(database, table)
        elif currentMode == 'isam':
            pass
            # isamList.append(tableNew)
            # return isam.dropTable(database, table)
        elif currentMode == 'json':
            pass
            # jsonList.append(tableNew)
            # return j.dropTable(database, table)
        elif currentMode == 'hash':
            pass
            # hashList.append(tableNew)
            # return Hash.dropTable(database, table)
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
            return DictMode.showTables(database)
        elif currentMode == 'isam':
            pass
            # isamList.append(tableNew)
            # return isam.showTables(database)
        elif currentMode == 'json':
            pass
            # jsonList.append(tableNew)
            # return j.showTables(database)
        elif currentMode == 'hash':
            pass
            # hashList.append(tableNew)
            # return Hash.showTables(database)
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
            return DictMode.alterAddPK(database, table, columns)
        elif currentMode == 'isam':
            pass
            # isamList.append(tableNew)
            # return isam.alterAddPK(database, table, columns)
        elif currentMode == 'json':
            pass
            # jsonList.append(tableNew)
            # return j.alterAddPK(database, table, columns)
        elif currentMode == 'hash':
            pass
            # hashList.append(tableNew)
            # return Hash.alterAddPK(database, table, columns)
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
            return DictMode.alterDropPK(database, table)
        elif currentMode == 'isam':
            pass
            # isamList.append(tableNew)
            # return isam.alterDropPK(database, table)
        elif currentMode == 'json':
            pass
            # jsonList.append(tableNew)
            # return j.alterDropPK(database, table)
        elif currentMode == 'hash':
            pass
            # hashList.append(tableNew)
            # return Hash.alterDropPK(database, table)
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
            return DictMode.insert(database, table, register)
        elif currentMode == 'isam':
            pass
            # isamList.append(tableNew)
            # return isam.insert(database, table, register)
        elif currentMode == 'json':
            pass
            # jsonList.append(tableNew)
            # return j.insert(database, table, register)
        elif currentMode == 'hash':
            pass
            # hashList.append(tableNew)
            # return Hash.insert(database, table, register)
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
            return DictMode.update(database, table, register, columns)
        elif currentMode == 'isam':
            pass
            # isamList.append(tableNew)
            # return isam.update(database, table, register, columns)
        elif currentMode == 'json':
            pass
            # jsonList.append(tableNew)
            # return j.update(database, table, register, columns)
        elif currentMode == 'hash':
            pass
            # hashList.append(tableNew)
            # return Hash.update(database, table, register, columns)
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
            return DictMode.delete(database, table, columns)
        elif currentMode == 'isam':
            pass
            # isamList.append(tableNew)
            # return isam.delete(database, table, columns)
        elif currentMode == 'json':
            pass
            # jsonList.append(tableNew)
            # return j.delete(database, table, columns)
        elif currentMode == 'hash':
            pass
            # hashList.append(tableNew)
            # return Hash.delete(database, table, columns)
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
            return DictMode.truncate(database, table)
        elif currentMode == 'isam':
            pass
            # isamList.append(tableNew)
            # return isam.truncate(database, table)
        elif currentMode == 'json':
            pass
            # jsonList.append(tableNew)
            # return j.truncate(database, table)
        elif currentMode == 'hash':
            pass
            # hashList.append(tableNew)
            # return Hash.truncate(database, table)
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
            return DictMode.alterAddColumn(database,table, default)
        elif currentMode == 'isam':
            pass
            # isamList.append(tableNew)
            # return isam.alterAddColumn(database,table, default)
        elif currentMode == 'json':
            pass
            # jsonList.append(tableNew)
            # return j.alterAddColumn(database,table, default)
        elif currentMode == 'hash':
            pass
            # hashList.append(tableNew)
            # return Hash.alterAddColumn(database,table, default)
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
            return DictMode.alterDropColumn(database, table, columnNumber)
        elif currentMode == 'isam':
            pass
            # isamList.append(tableNew)
            # return isam.alterDropColumn(database, table, columnNumber)
        elif currentMode == 'json':
            pass
            # jsonList.append(tableNew)
            # return j.alterDropColumn(database, table, columnNumber)
        elif currentMode == 'hash':
            pass
            # hashList.append(tableNew)
            # return Hash.alterDropColumn(database, table, columnNumber)
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
            return DictMode.extractTable(database, table)
        elif currentMode == 'isam':
            pass
            # isamList.append(tableNew)
            # return isam.extractTable(database, table)
        elif currentMode == 'json':
            pass
            # jsonList.append(tableNew)
            # return j.extractTable(database, table)
        elif currentMode == 'hash':
            pass
            # hashList.append(tableNew)
            # return Hash.extractTable(database, table)
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
            return DictMode.extractRangeTable(database, table, columnNumber, lower, upper)
        elif currentMode == 'isam':
            pass
            # isamList.append(tableNew)
            # return isam.extractRangeTable(database, table, columnNumber, lower, upper)
        elif currentMode == 'json':
            pass
            # jsonList.append(tableNew)
            # return j.extractRangeTable(database, table, columnNumber, lower, upper)
        elif currentMode == 'hash':
            pass
            # hashList.append(tableNew)
            # return Hash.extractRangeTable(database, table, columnNumber, lower, upper)
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
            return DictMode.extractRow(database, table, columns)
        elif currentMode == 'isam':
            pass
            # isamList.append(tableNew)
            # return isam.extractRow(database, table, columns)
        elif currentMode == 'json':
            pass
            # jsonList.append(tableNew)
            # return j.extractRow(database, table, columns)
        elif currentMode == 'hash':
            pass
            # hashList.append(tableNew)
            # return Hash.extractRow(database, table, columns)
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
            return DictMode.loadCSV(file,database,table)
        elif currentMode == 'isam':
            pass
            # isamList.append(tableNew)
            # return isam.loadCSV(file,database,table)
        elif currentMode == 'json':
            pass
            # jsonList.append(tableNew)
            # return j.loadCSV(file,database,table)
        elif currentMode == 'hash':
            pass
            # hashList.append(tableNew)
            # return Hash.loadCSV(file,database,table)
    else:
        return 2

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
    # elif mode == 'isam':
    #     if isam.createDatabase(database) == 0:
    #         isamList.append(database)
    #         return 0
    #     else:
    #         return isam.createDatabase(database)
    # elif mode == 'json':
    #     if j.createDatabase(database) == 0:
    #         jsonList.append(database)
    #         return 0
    #     else:
    #         return j.createDatabase(database)
    # elif mode == 'hash':
    #     if Hash.createDatabase(database) == 0:
    #         hashList.append(database)
    #         return 0
    #     else:
    #         return Hash.createDatabase(database)

def searchInMode(value):
    if value in avlList:
        return 'avl'
    elif value in bList:
        return 'b'
    elif value in bplusList:
        return 'bplus'
    elif value in dictList:
        return 'dict'
    else:
        return None