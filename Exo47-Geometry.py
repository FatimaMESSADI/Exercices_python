from math import sqrt
class Geometry(object):
      #contructeur par défaut


      #une méthode pour calculer la puissance 2
      def puissance(self, p):
          return p*p
      #calculer la distance entre deux points
      def distance(self, x1, y1, x2, y2):
          return sqrt(self.puissance(x2-x1) - self.puissance(y2-y1))
      #calculer le mileu de deux points
      def middle(self, x1, y1, x2, y2):
          return x1+x2/2, y1+y2/2

      #calculer le primètre d'un triangle
      def perTriangle(self, x1, y1, z1, x2, y2, z2):

          a = self.distance(x1,y1,x2,y2)
          #print("distance 1 =", a)
          b = self.distance(x1,z1,x2,z2)
          #print("distance 2 =", b)
          c = self.distance(z1,y1,z2,y2)
          #print("distance 3 =", c)


          return a + b + c
      #vérifier si le triangle est isocèle
      def triangleIsosce(self, x1, y1, z1, x2, y2, z2):

          a1 = self.distance(x1,y1,x2,y2)
          b1 = self.distance(x1,z1,x2,z2)
          c1 = self.distance(z1,y1,z2,y2)
          if a1 == b1 or a1 == c1 or b1 == c1:
              return True
          else:
              return False




#instance
g = Geometry()
print("Distance value is:", g.distance(2,6,5,4))
print("---------------------------------------")
print("Middle value is:", g.middle(2,6,5,4))
print("----------------------------------------")
print("Perimeter value is:", g.perTriangle(4,5,6,8,7,9))
print("---------------------------------------")
print("This triangle is  isoscel?\n", g.triangleIsosce(4,5,6,8,7,9))
