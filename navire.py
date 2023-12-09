class Course:
    
    def __init__(self, category):
        self.category = category
        self.bateaux = set()
        self.match_category = {
            '2x': Bateau2x,
            '2-': Bateau2,
            '1x': BateauSkiff
        }
        self.demarre = False
        self.elapsed_time = 0

    def ajout_bateau_ligne_depart(self, bateau):
        if isinstance(bateau, self.match_category[self.category]):
            self.bateaux.add(bateau)
            print(f'Bateau {bateau} bon')
        else:
            print(f'Bateau {bateau} n\'est pas bon.')


    def depart(self):
        if len(self.bateaux) > 1:
            self.demarre = True

    def en_cours(self):
        return self.demarre

    def next_loop(self):
        self.demarre = False
        self.elapsed_time += 1
        for bateau in self.bateaux:
            elapsed_distance = (self.elapsed_time * 500) / bateau.get_average_speed()
            if elapsed_distance < 2000:
                self.demarre = True
            else:
                break

    def affiche_positions(self):
      print(f'Temps écoulé : {self.elapsed_time}')
      grid_sorted = list(self.bateaux)
      grid_sorted.sort(key=Bateau.get_average_speed, reverse=True)
      for idx, bateau in enumerate(grid_sorted):
            print(f'{idx}: {bateau}')

    
    def vainqueur(self):
        return max(self.bateaux, key=Bateau.get_average_speed)

    def run(self):
        self.depart() 
        while self.en_cours():
            self.next_loop() 
            print(self.affiche_positions())
            # affiche le nom du bateau et sa distance parcourue
            # mickey,10
            # minnie,20
            # affiche le nom du plus rapide: minnie
        print(self.vainqueur())

class Bateau:
    
    def __init__(self, capitain, average_speed):
        self.capitain = capitain
        self.average_speed = average_speed

    def get_average_speed(self):
        return self.average_speed
    
    def set_average_speed(self, new_average_speed):
        if (new_average_speed > 0):
            self.average_speed = new_average_speed
        else:
            print('mais avancez la !!')

    def __repr__(self):
        return self.capitain
    
    def __gt__(self, other):
        return self.average_speed > other.average_speed

class Bateau2x(Bateau):

    def __init__(self, capitain, average_speed):
        super().__init__(capitain, average_speed)

class Bateau2(Bateau):

    def __init__(self, capitain, average_speed):
        super().__init__(capitain, average_speed)


class BateauSkiff(Bateau):

    def __init__(self, capitain, average_speed):
        super().__init__(capitain, average_speed)


if __name__ == '__main__':
    course_cadets = Course('2x')
    bateau_1_2x = Bateau2x('mickey', 62)
    bateau_2_2x = Bateau2x('minnie', 70)
    bateau_3_skiff = BateauSkiff('picsou', 120)
    course_cadets.ajout_bateau_ligne_depart(bateau_1_2x)
    course_cadets.ajout_bateau_ligne_depart(bateau_2_2x)
    course_cadets.ajout_bateau_ligne_depart(bateau_3_skiff)
    # affichage d'un message
    # le bateau n'a pas pu être ajouté
    # mais continue l'exécution de l'application
    course_cadets.run()
