from math import *
class Point(object):
    x : float
    y : float
    def __init__(self, abs, ord):
        self.x = abs
        self.y = ord
    def afficher(self):
        print("POINT(X = " + str(self.x) + ', Y = ' + str(self.y) + ')')

class Cercle:
    centre : Point
    rayon : float
    def __init__(self,centre,rayon):
        self.centre = centre
        self.rayon = rayon
    def getPerimetre(self):
        return 2*pi*self.rayon
    def getSurface(self):
        return pi*pow(self.rayon,2)
    def appartient(self, p:Point):
        if(sqrt(pow(self.centre.x - p.x, 2) + pow(self.centre.y - p.y, 2)) == self.rayon):
            return True
        else:
            return False
    def afficher(self):
        print("CERCLE(X = " + str(self.centre.x) + ', Y = ' + str(self.centre.y) + ', R = ' +  str(self.rayon) + ')')
class Cylindre(Cercle):
    hauteur : float
    def __init__(self, centre, rayon,  hauteur):
        Cercle.__init__(self, centre, rayon)
        self.hauteur = hauteur
    def getVolume(self):
        return pi * pow(self.rayon,2) * self.hauteur
if __name__ == '__main__':
    A = Point(4.0, 6.0)
    B = Point(4.0, 4.0)
    A.afficher()
    myCercle = Cercle(A,6)
    print("Perimetre du cercle : ", myCercle.getPerimetre())
    print("Surface du cercle : ", myCercle.getSurface())
    print("Le point appartient-il au cercle ? " + str(myCercle.appartient(B)))
    myCercle.afficher()
    cylindre = Cylindre(A,2.0,3.0)
    print("Volume du cylindre : ", cylindre.getVolume())
    
    
        
    



    


