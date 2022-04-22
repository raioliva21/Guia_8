#from main import Juego
import random

from numpy import isin

from arma import Arma

"""<x coordinate> y <y coordinate>"""
class Alien():

    def __init__(self, x_coordinate, y_coordinate):
        self._x_coordinate = x_coordinate
        self._y_coordinate = y_coordinate
        self._health = 3
        self._collision_detection = None
        self._total_aliens_created = 0
        self._armas = []
    
    @property
    def health(self):
        print(self._health)
    
    @property
    def x_coordinate(self):
        return self._x_coordinate

    @x_coordinate.setter
    def x_coordinate(self, coordenada_x):
        if isinstance (coordenada_x, int):
            if 0 <= coordenada_x <= 15:
                self._x_coordinate = coordenada_x
            else:
                print("Coordenada 'x' ingresada supera limite.")
        else:
            return False
    
    @property
    def y_coordinate(self):
        return self._y_coordinate
    
    @y_coordinate.setter
    def y_coordinate(self, coordenada_y):
        if isinstance (coordenada_y, int):
            if 0 <= coordenada_y <= 15:
                self._y_coordinate = coordenada_y
            else:
                print("Coordenada 'y' ingresada supera limite.")
        else:
            return False
    
    def hit(self):
        # vida de objeto alien no puedo ser menor a 0
        if self._health >= 1:
            self._health = self._health - 1
    
    def is_alive(self):
        if self._health > 0:
            print(True)
        else:
            print(False)
    
    def teleport(self, value_x, value_y):
        self.x_coordinate = value_x
        self.y_coordinate = value_y


    def ataque(self, coor_x_atq, coor_y_atq):
        self._coor_ataque = [coor_x_atq, coor_y_atq]

    def collision_detection(self, coor_x_atq, coor_y_atq):
        self._collision = [coor_x_atq, coor_y_atq]
        if isinstance (self._collision, Alien):
            if self._collision[0] == self._x_coordinate and\
                self._collision[0] == self._y_coordinate:
                self.hit()
    
    @property
    def armas(self):
        self._armas
    
    @armas.setter
    def armas(self, arma):
        if isinstance(arma, Arma):
            self._armas.append(arma)