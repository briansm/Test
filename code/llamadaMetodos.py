from modeBTree import *

insertar = createDatabase('db1')
print(insertar)
insertar1 = createDatabase('db1')
print(insertar1)
insertar2 = createDatabase('db4')
print(insertar2)
insert = createDatabase('db5')
print(insert)
ingresar = createDatabase(0)
print(ingresar)
alter = alterDatabase('db5', 'db1')
print(alter)
alter1 = alterDatabase('db5', 'db2')
print(alter1)
drop = dropDatabase('db4')
print(drop)
imp = showDatabases()
print(imp)


#--tablas
print("\n-----")
print(createTable("db1","table1",4))
print(createTable("db1","table2",5))
print(createTable("db2","table3",9))
print(createTable("db2","table4",2))
print(createTable("db3","table5",3))

print(showTables("db1"))
print(showTables("db2"))
#print(extractTable("db1", "table1"))
#print(extractRangeTable("bd1","tabla1",2,0,2))
print(alterTable("db1","table1","tableNew"))
#alterAddColumn(database, table, columnNumber) :
#print(alterDropColumn("db1", "table1", 2))
print(dropTable("db1","table1"))
print(dropTable("db1","table2"))