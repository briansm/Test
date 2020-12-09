class NodoLista :
    def __init__(self,valorIngresado) :
        #Este es mi cambio
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
        #cambio desde dekstop
        # if we can read this  its ok :)  
        print("hola mundo x10")
        print("hola mundo x20")
        print("hola mundo x30")
        print("hola mundo x40")
        print ("intento")
        #prueba gley 

        pass


    # Buscar un nodo, retorna true/false [JORGE]
    # ------- se deberia de ver el cambio no?
    def metodoJ(self):
        print("Metodo nuevo modificado por mi, Jorge :v")
    def buscarNodo(self,valorABuscar) : 
        print("listo")
        print("prro!!! ahorita vi los cambios que hice")
        # ------ espero que estos se vean

        print('bandaaaaaa')



        print('este es el cambio luego de los cambios :v')

    # Imprimir Lista: 8->3->5->1 [DIEGO]
    def mostrarNodosSiguientes(self) : 
        print('Hola mundo')
        #prueba No 99999
        #esta se´ria una preueba mas

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


