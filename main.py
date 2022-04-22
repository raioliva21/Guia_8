from alien import Alien
import random

from canon_de_protones import Canon
from granada_antimateria import Granada
from pistola_laser import Pistola


class Juego():


    def __init__(self):
        
        coordenada_x = random.randint(0,15)
        coordenada_y = random.randint(0,15)
        self._armas = []

        alien = Alien(coordenada_x, coordenada_y)
        #other_object = Other_object()


        alien_start_positions = [(4,7), (3,0)]
        self.aliens = self.new_aliens_collection\
            (alien_start_positions)
        
        #print("imprime coordenadas")
        for alien in self.aliens:
            print(alien.x_coordinate, alien.y_coordinate)
        
        self.total_aliens_created()

        armas = [Canon(), Granada(), Pistola()]

        """
        for alien in self.aliens:
            cantidad_armas = random.choice(2)
            for indice in range(0,cantidad_armas):
                alien.armas = armas[indice]
        """
        #print(type(alien[0]))
        alien1 = self.aliens[0]
        alien2 = self.aliens[1]
        


    def new_aliens_collection(self, alien_start_positions):

        # alien_start_positions son coordenadas
        aliens = []
        for coordenada in alien_start_positions:
            aliens.append(Alien(coordenada[0],coordenada[1]))

        # retorna lista de objetos clase alien
        return aliens
    
    def total_aliens_created(self):
        return print(len(self.aliens))



juego = Juego()