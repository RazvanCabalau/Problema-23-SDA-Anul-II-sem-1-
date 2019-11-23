from problem import Problem
import random
from itertools import chain, combinations
import collections
class Problema23(Problem):
    def __init__(self):
        n = random.randint(8, 12)
        datagen = random.sample(range(12), n)
        data = (datagen)
        statement = 'Primiti vectorul: ' + ', '.join(map(str, data[0])) + '. '
        statement += 'Faceti din acest vector un min-ansamblu folosind\n un numar minim de operatii si demonstrati complexitatea.\n'
        statement += '\n'

        super().__init__(statement, data)

    def solve(self):




        return 0