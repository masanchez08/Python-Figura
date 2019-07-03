##import Circulo
import cuadrado
import rectangulo
import Figura as f
import punto

class Main:


    print (" Seleccione la figura:")
    print (" 1.Cuadrado ")
    print (" 2.Rectangulo ")
    print (" 3.Circulo ")
    
    num= input("Ingrese un numero del 1 al 3: ")
    origen =punto.punto()
    fin =punto.punto()
    

    def mostrar(f, origen, fin):
        f.origen()
        f.setFin()
        f.calcularArea()
        f.calcularPerimetro()
        print ("El area es ",area)
        print ("El perimetro es ",perimetro)

    if num==1:
        f =cuadrado.cuadrado()
        origen.setX=0
        origen.setX=0
        fin.setX=5
        fin.setY=0
        mostrar(f, origen, fin)
    
    elif num==2:
        f = rectangulo.rectangulo()
        origen.setX=0
        origen.setY=5
        fin.setX=10
        fin.setY=0
        mostrar(f, origen, fin)
    
    elif num==3:
        f =circulo.circulo()
        origen.setX=0
        origen.setY=0
        fin.setx=9
        fin.setY=0
        mostrar(f, origen, fin)
    
    else:
        print ("Opcion no valida ")
       
