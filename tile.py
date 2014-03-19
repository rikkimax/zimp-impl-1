#------------------------------------------------------------------------------
# Name:        tile
# Purpose:     choosing tiles
#
# Author:      framework = Richard Cattermole
#              content code = Loki Kristianson
#
# Created:     19/03/2014
# Copyright:   (c)
#
#------------------------------------------------------------------------------


import random

indoor = [
    [0, 'Foyer', True, False, False, False, False],
    [0, 'Family Room', True, True, False, True, False],
    [0, 'Kitchen', True, True, False, True, True],
    [0, 'Bedroom', True, False, False, True, False],
    [0, 'Bathroom', True, False, False, False, False],
    [0, 'Storage', True, False, False, False, False],
    [0, 'Evil Temple', False, True, True, False],
    [0, 'Dining Room', True, True, True, True, False]
]

outdoor = [
    [1, 'Patio', True, True, True, False, False],
    [1, 'Garage', False, False, True, True, False],
    [1, 'Sitting Area', False, True, True, True, False],
    [1, 'Garden', False, True, True, True, True],
    [1, 'Yard1', False, True, True, True, False],
    [1, 'Yard2', False, True, True, True, False],
    [1, 'Yard3', False, True, True, True, False],
    [1, 'Graveyard', False, True, True, True, False]
]

# The following code is to show output - will be dealt with in gamestate

current_area = []


class Tile:

    def __init__(self, type, name, door_top, door_right, door_bottom,
                 door_left, add_1_health):
        self.type = type
        self.name = name
        self.door_top = door_top
        self.door_right = door_right
        self.door_bottom = door_bottom
        self.door_left = door_left
        self.add_1_health = add_1_health
        #self.may_resolve_card = may_resolve_card
        print ('The initial room is the ' + self.name)
        current_area = area[0]
        print (current_area)

    def on_resolve_card(self, card):
        """
        Rikki, not 100% sure what is needed here yet, but figure out

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
        #for num in range(1, len(area)):
        del area[x]  # Takes foyer/patio out of equasion, and after that
                         #  each room as it is chosen
        x = random.randrange(0, len(area), 1)
        print ("The next random room chosen is the " + area[x][1])
        current_area = area[x]
        print ("The details of this room are " + str(current_area))
        return

area = indoor  # To change to outdoor when going out with totem
which_tile = Tile(*area[0])  # Chooses initial Foyer or Patio
which_tile.find_next()  # Randomly chooses next room/garden area
