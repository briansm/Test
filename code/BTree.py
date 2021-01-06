import os
class NodeBTree :
    def __init__(self) :
        self.gradeTree = 4
        self.maxKeys = self.gradeTree -1
        self.keys = []
        self.children = []
        self.parentNode = None

class Registro:
    def __init__(self,listRegister):
        self.register = listRegister
        self.idHide = 0

class BTree :
    
    def __init__(self):
        self.root = None
        self.identity = 0
        self.maxColumna = 0
        self.listRegister = []
        self.columPK = [0]

    def isTreeEmpty(self) :
        if self.root is None:
            return True
        else:
            return False
    
    def searchNodeToInsert(self,currentRegister,currentNode) :
        
        maxKeys = len(currentNode.keys)
        i = 0
        while i <  maxKeys and currentNode.keys[i].register[0] < currentRegister.register[0]:
            i += 1
        if i < maxKeys and currentNode.keys[i].register[0] == currentRegister.register[0]:
            return currentNode.keys[i].register
        if len(currentNode.children) == 0:
            return currentNode
        else: 
            return self.searchNodeToInsert(currentRegister,currentNode.children[i])
    
    def changeTypePK(self,currentRegister):
        if currentRegister.register[self.columPK[0]].isdigit():
            currentRegister.register[self.columPK[0]] = int(currentRegister.register[self.columPK[0]])

    def insertSorted(self,register,currentNode,childNode) :
        pivote = 0
        if len(currentNode.keys) == 0:
            currentNode.keys.append(register)
        else:
            # Encuentra la posicion del valor mayor a el
            while currentNode.keys[pivote].register[self.columPK[0]] < register.register[self.columPK[0]] :
                pivote += 1
                #desborda el indice
                if pivote > len(currentNode.keys) -1 :
                    break
            currentNode.keys.append(None)
            #desplaza una pos hacia adelante cada clave
            for i in range( len(currentNode.keys) -1, pivote-1 , -1 ):
                currentNode.keys[i] = currentNode.keys[i-1]
            if childNode is not None:
                currentNode.children.append(None)
                #desplaza una pos hacia adelante cada hijo
                for i in range( len(currentNode.children) -1, pivote , -1 ):
                    currentNode.children[i] = currentNode.children[i-1]
                #agrega un nuevo nodo en una pos ordenada del nodo padre
                currentNode.children[pivote+1] = childNode
            #agrega una nueva clave en una pos ordenada
            currentNode.keys[pivote] = register

    def splitCurrentNode(self,nodeToSplit) :
        rightNode = NodeBTree()
        leftNode = NodeBTree()
        MINUSCHILDREN = int(((nodeToSplit.gradeTree/2) - 1) + 1)
        for i in range(MINUSCHILDREN,nodeToSplit.gradeTree+1):
            rightNode.keys.append(nodeToSplit.keys[MINUSCHILDREN])
            del nodeToSplit.keys[MINUSCHILDREN]
            if len(nodeToSplit.children) != 0:
                rightNode.children.append(nodeToSplit.children[MINUSCHILDREN+1]) 
                del nodeToSplit.children[MINUSCHILDREN+1]
        newParent = NodeBTree()
        newParent.keys.append(rightNode.keys[0])
        leftNode = nodeToSplit
        rightNode.parentNode = newParent.parentNode
        del rightNode.keys[0]
            
        if nodeToSplit.parentNode is None:
            self.root = newParent
            leftNode.parentNode = self.root
            rightNode.parentNode = self.root
            
            self.root.children.append(leftNode)
            self.root.children.append(rightNode)
        else:
            parent = nodeToSplit.parentNode
            self.insertSorted(newParent.keys[0],parent,rightNode)
            rightNode.parentNode = parent
            del newParent
            if len(parent.keys) > parent.gradeTree:
                self.splitCurrentNode(parent)

    def insertSubtree(self,value,currentNode) :
        # Nodo es una hoja o raiz
        if len(currentNode.children) == 0 :
            self.insertSorted(value,currentNode,None)
        else: 
            nodeToInsert = self.searchNodeToInsert(value,currentNode)
            self.insertSubtree(value,nodeToInsert)
        if len(currentNode.keys) > currentNode.gradeTree:
            self.splitCurrentNode(currentNode)
            

    def insertNode(self,currentRegister) :
        self.identity += 1
        currentRegister.idHide = self.identity
        self.listRegister.append(currentRegister)
        # print("{} {}".format(currentRegister.idHide,currentRegister.register))
        if self.isTreeEmpty() :
            newNode = NodeBTree()
            newNode.keys.append(currentRegister) 
            self.root = newNode
        else:
            self.insertSubtree(currentRegister,self.root)
    
    def graphBTree(self):
        temp = self.root
        
        f = open("Arbol.dot","w")
        f.write("digraph g{\n")
        f.write("node [shape = rect, width=1, height=0.4];\n")
        f.write("rankdir=UP;\n")
        
        if temp is not None:
            f.write("\"")
            for i in range(len(temp.keys)):
                f.write(str(temp.keys[i].register)+"|")
            f.write("\"")

            
            if len(temp.children) != 0:
                # print(len(temp.children))
                f.write("->{")

                f.write("\"")
                for i in range(len(temp.children)):
                    for j in range(len(temp.children[i].keys)):
                            f.write(str(temp.children[i].keys[j].register)+"|")
                    if i == len(temp.children)-1:
                        break
                    f.write("\" \"")
                f.write("\"};\n")
                
                if  len(temp.children[0].children) != 0 :
    # ----------------------------------------------------------------------------
                    f.write("\"")
                    for i in range(len(temp.children[0].children)-1):
                        f.write(str(temp.children[0].keys[i].register)+"|")
                    f.write("\"")

                    f.write("->{")
                    
                    f.write("\"")
                    if len(temp.children[0].children) != 0:
                        for i in range(len(temp.children[0].children)):
                            for j in range(len(temp.children[0].children[0].keys)):
                                f.write(str(temp.children[0].children[i].keys[j].register)+"|")
                            if i == len(temp.children[0].children[0].keys):
                                break
                            f.write("\" \"")
                    f.write("\"};\n")
    # ----------------------------------------------------------------------------
                    f.write("\"")
                    for i in range(len(temp.children[1].children)-1):
                        f.write(str(temp.children[1].keys[i].register)+"|")
                    f.write("\"")

                    f.write("->{")
                    
                    f.write("\"")
                    if len(temp.children[1].children) != 0:
                        print("HOLA {}".format(len(temp.children[0].keys)))
                        for i in range(len(temp.children[1].children)):
                            for j in range(len(temp.children[1].children[0].keys)):
                                f.write(str(temp.children[1].children[i].keys[j].register)+"|")
                            if i == len(temp.children[1].children[0].keys):
                                break
                            f.write("\" \"")
                    f.write("\"};\n")
        f.write("}")
        f.close()
        os.system("dot -Tjpg Arbol.dot -o Arbol.jpg")

#Funcion general para realizar busquedas para extratcRow, update y delete
    def searchRegistro(self,ValorDeLlave,currentNode) :
        # ValorBuscado = str(ValorDeLlave)
        if currentNode is not None:
            maxKeys = len(currentNode.keys)
            i = 0

            while i <  maxKeys and currentNode.keys[i].register[0] < ValorDeLlave:
                i += 1
            if i < maxKeys and currentNode.keys[i].register[0] == ValorDeLlave:
                return currentNode.keys[i]
            if len(currentNode.children) == 0:
                return None
            else: 
                return self.searchRegistro(ValorDeLlave,currentNode.children[i])


    def insert(self, register):
        #if buscarNodo(database):
            #if buscarTablas(table):
        # try:
            if len(register) <= self.maxColumna:
                miRegister = Registro(register)
                self.changeTypePK(miRegister)
                self.insertNode(miRegister)
                return 0
            else:
                return 5
        # except :
        #     return 1
    
    
    def extractRow(self, columns):
        #if buscarNodo(database):
            #if buscarTablas(table):

                #try:

                    registroEncontrado = self.searchRegistro(columns[0], self.root)


                    if registroEncontrado != None:
                        return registroEncontrado.register
                    else:
                        return []
                #except:
                    #return []


    #Carga de archivo
    def loadCSV(self, filepath):
        try:
            res = []
            import csv
            with open(filepath, 'r') as file:
                reader = csv.reader(file, delimiter = ',')
                for row in reader:
                    res.append(self.insert(row))
            return res
        except:
            return []

    #Busqueda y actiualizacion de datos almacenados en el arbol
    def update(self, register, columns):
        #if buscarNodo(database):
            #if buscarTablas(table):
            
                try:
                    registroEncontrado = self.searchRegistro(columns[0], self.root)


                    if registroEncontrado != None:

                        for clave in register:
                            registroEncontrado.register[clave] = register[clave]
                
                    return 0
                
                except:
                    return 1
            #else:

                #return 3

        #else:
            #return 2


    #Busqueda y eliminacion de registros almacenados en arbol
    def delete(self, database, table, columns):
        
        try:
            registroEncontrado = self.searchRegistro(columns[0], self.root)

            if registroEncontrado != None:
                del registroEncontrado
                return 0
        except:
            return 1



    def truncate (self, database, table):
        try:
            self.root = None
            return 0
        except:
            return 1

# if __name__ == "__main__":
    # miRegister = Registro([33,"Steve","Morales"])
    # miRegister2 = Registro([11,"Peter","Morales"])
    # miRegister3 = Registro([3,"Ariadna","Samayoa"])
    # miRegister4 = Registro([21,"Csterion","Morales"])
    # miRegister5 = Registro([4,"Luis","Morales"])
    # miRegister6 = Registro([5,"Jaime","Samayoa"])
    # miRegister7 = Registro([25,"Brian","Samayoa",25])
    # miRegister8 = Registro([6,"Brian","Samayoa",25])
    # miRegister9 = Registro([1,"Brian","Samayoa",25])
    # miRegister10 = Registro([34,"Brian","Samayoa",25])
    # miRegister11 = Registro([36,"Brian","Samayoa",25])
    # miRegister12 = Registro([38,"Brian","Samayoa",25])
    # miRegister13 = Registro([22,"Brian","Samayoa",25])
    # miRegister14 = Registro([23,"Brian","Samayoa",25])
    # miRegister15 = Registro([20,"Brian","Samayoa",25])
    # miRegister16 = Registro([40,"Brian","Samayoa",25])
    # miRegister17 = Registro([41,"Brian","Samayoa",25])
    # miRegister18 = Registro([80,"Brian","Samayoa",25])
    # miRegister19 = Registro([101,"Brian","Samayoa",25])
    # miRegister20 = Registro([103,"Brian","Samayoa",25])
    # miRegister21 = Registro([600,"Brian","Samayoa",25])
    # miRegister22 = Registro([300,"Brian","Samayoa",25])
    # miArbol = BTree()
    # miArbol.insertNode(miRegister)
    # miArbol.insertNode(miRegister2)
    # miArbol.insertNode(miRegister3)
    # miArbol.insertNode(miRegister4)
    # miArbol.insertNode(miRegister5)
    # miArbol.insertNode(miRegister6)
    # miArbol.insertNode(miRegister7)
    # miArbol.insertNode(miRegister8)
    # miArbol.insertNode(miRegister9)
    # miArbol.insertNode(miRegister10)
    # miArbol.insertNode(miRegister11)
    # miArbol.insertNode(miRegister12)
    # miArbol.insertNode(miRegister13)
    # miArbol.insertNode(miRegister14)
    # miArbol.insertNode(miRegister15)
    # miArbol.insertNode(miRegister16)
    # miArbol.insertNode(miRegister17)
    # miArbol.insertNode(miRegister18)
    # miArbol.insertNode(miRegister19)
    # miArbol.insertNode(miRegister20)
    # miArbol.insertNode(miRegister21)
    # miArbol.graphBTree()
    # print(miArbol.listRegister)
    # miArbol = BTree()
    # miArbol.columPK = [0]
    # print(50*"-"+"Insertar"+50*"-")
