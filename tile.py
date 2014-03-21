#------------------------------------------------------------------------------
# Name:        tile
# Purpose:     choosing tiles
#
# Author:      framework = Richard Cattermole
#              content code = Loki Kristianson
#
# Created:     19/03/2014
#
#
#------------------------------------------------------------------------------


import random

area = [
    [0, 'Foyer', True, False, False, False, False],
    [1, 'Patio', True, True, True, False, False],
    [2, 'Evil Temple', False, True, True, False],
    [3, 'Storage', True, False, False, False, False],
    [4, 'Kitchen', True, True, False, True, True],
    [5, 'Dining Room', True, True, True, True, False],
    [6, 'Garden', False, True, True, True, True],
    [7, 'Graveyard', False, True, True, True, False]
]

forgotten_area = [
    [8, 'Family Room', True, True, False, True, False],
    [8, 'Bedroom', True, False, False, True, False],
    [8, 'Bathroom', True, False, False, False, False],
    [8, 'Garage', False, False, True, True, False],
    [8, 'Sitting Area', False, True, True, True, False],
    [8, 'Yard1', False, True, True, True, False],
    [8, 'Yard2', False, True, True, True, False],
    [8, 'Yard3', False, True, True, True, False],

]

current_area = []


class Tile:

    def __init__(self, id):
        self.type = id
        self.name = area[id][1]
        print ('The initial room is the ' + self.name)
        current_area = area[0]
        print ('The details of this room are ' + str(current_area) + '\n')

    def on_resolve_card(self, card):
        """
        Rikki & Claire, I'll have this function done Saturday morning

        When a dev card has been solved call this.
        Allows for events on this instance.
        """
        pass

    def find_next(self):
        """
        Randomly chooses a new Tile card.
        This does not apply to the Foyer and Patio.
        Returns:
            A new Tile instance
        """
        global area
        global current_area
        x = 0
        for num in range(1, len(area)):
            del area[x]  # Takes foyer out of equasion, and after that
                         #  each room as it is chosen
            x = random.randrange(0, len(area), 1)
            if area[x][1] == "Patio":
                print ("Patio is chosen but will be skipped and used later")
            else:
                print ("The next random room chosen is the " + area[x][1])
                current_area = area[x]
                print ("The details of this room are " + str(current_area))
        return

which_tile = Tile(0)  # Chooses initial Foyer
which_tile.find_next()  # Randomly chooses next room/garden area
