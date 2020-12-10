class NodoLista :
    def __init__(self,valorIngresado) :
        self.valorIngresado = valorIngresado
        self.siguiente = None
        self.anterior = None

class ListaDoble :
    def __init__(self) :
        self.primerNodo = None
        self.ultimoNodo = None
    
    def esListaVacia(self) :   
        if self.primerNodo is None :
            return True
        else :
            return False

    # Agregar nodo al final de la lista [GLEIMY]
    def agregarNodo(self,valorIngresado):
        pass
    
    # Buscar un nodo, retorna true/false [JORGE]
    def buscarNodo(self,valorABuscar) :
        self.aux = self.primerNodo
        while True :
            if self.aux.valorIngresado == valorABuscar :
                return True
            self.aux = self.aux.siguiente
        return False

    # Imprimir Lista: 8->3->5->1 [DIEGO]
    def mostrarNodosSiguientes(self) :
        pass

    # Imprimir Lista: 1->5->3->8 [EDGAR]
    def mostrarNodosAnteriores(self) :
    	print("prueba git")
        pass

if __name__ == "__main__":
    #miLista = ListaDoble()
    #miLista.agregarNodo(8)
    #miLista.agregarNodo(3)
    #miLista.agregarNodo(5)
    #miLista.agregarNodo(1)
    #print( miLista.buscarNodo(0) )
    # miLista.mostrarNodosAnteriores()
    # miLista.mostrarNodosSiguientes()
    pass