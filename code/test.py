class NodoLista :
    def __init__(self,valorIngresado) :
        self.valorIngresado = valorIngresado
        self.siguiente = None
        self.anterior = None

class ListaDoble :
    def __init__(self) :
        self.primerNodo = None
        self.ultimoNodo = None
    
    # Retornar true/false
    def esListaVacia(self) :   
        if self.primerNodo is None :
            return True
        else :
            return False

    # Agregar nodo al final de la lista [GLEIMY]
    def agregarNodo(self,valorIngresado):
        print ("intento")
        pass

    # Buscar un nodo, retorna true/false [JORGE]
    # --- prro!!!!
    def buscarNodo(self,valorABuscar) : 
        print("listo")
        print("prro!!! ahorita vi los cambios que hice")
        # ------ espero que estos se vean

    # Imprimir Lista: 8->3->5->1 [DIEGO] Solo toy viendo :3
    def mostrarNodosSiguientes(self) : 
        print('Hola mundo')
        #este vendria siendo una prueba mas :3 AAAAAAAAAAAAAAA

    # Imprimir Lista: 1->5->3->8 [EDGAR]
    def mostrarNodosAnteriores(self) :
        pass
    


    if __name__ == "__main__":
        pass
        # miLista = ListaDoble()
        # miLista.agregarNodo(8)
        # miLista.agregarNodo(3)
        # miLista.agregarNodo(5)
        # miLista.agregarNodo(1)
        # print( miLista.buscarNodo(0) )
        # miLista.mostrarNodosAnteriores()
        # miLista.mostrarNodosSiguientes()

