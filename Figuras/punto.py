from math import *
class Punto():
    
    def __init__(self):
        self.x = 0
        self.y = 0

    def getX(self,x):
        return self.x
    

    def setX(self,x):
        self.x = x
    

    def getY(self):
        return self.y
    

    def setY(self,y):
        self.y = y
        
    def calcularDistancia(self,p):
        return sqrt((self.x - p.getX())**2+(self.y - p.getY())**2)


    
