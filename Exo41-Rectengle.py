#la classe mère
class Rectengle(object):
    #constructeur
    def __init__(self, length, width):
        self.length = length
        self.width = width
    #une fonction pour calculer le périmètre
    def perimeter(self):
        return ( self.length + self.width ) * 2

    #une fonction pour calculer la surface
    def area(self):
        return self.length * self.width

    #une fonction d'affichage
    def Display(self):

        print("length value is-->", self.length)
        print("width value is -->", self.width)
        print("perimeter value is -->", self.perimeter())
        print("area value is -->", self.area())

#instances
rect = Rectengle(7 , 5)
rect.Display()

#la class enfant
class Parallelepipede(Rectengle):
    #le constructeur
    def __init__(self, length, width , height):
        #appel du contructeur de la classe mère
        Rectengle.__init__(self, length, width)
        self.height = height

    #une fonction pour calculerle volume du Parallelepipede
    def Volume(self):

        return self.length * self.width * self.height
    #Afficher le volume
    def Display_(self):
        print("volume value is-->", self.Volume())


#instances
Paral = Parallelepipede(7,4,7)
Paral.Display_()
