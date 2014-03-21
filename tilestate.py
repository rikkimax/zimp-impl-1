#------------------------------------------------------------------------------
# Name:        tilestate
# Purpose:
#
# Author:      framework = Richard Cattermole
#              content code = Loki Kristianson
#
# Created:     19/03/2014
# Copyright:   (c)
#
#------------------------------------------------------------------------------


#from defs import Direction
import tile


import tile


class TileState:

    def __init__(self, tile, rotation, left, right, top, bottom,
                 has_item_been_found):
        self.tile = tile
        self.rotation = rotation
        if rotation == 1:
            self.left = left
            self.right = right
            self.top = top
            self.bottom = bottom
        elif rotation == 2:
            self.left = bottom
            self.right = top
            self.top = left
            self.bottom = right
        elif rotation == 3:
            self.left = right
            self.right = left
            self.top = bottom
            self.bottom = top
        else:
            self.left = top
            self.right = bottom
            self.top = right
            self.bottom = left
        self.has_item_been_found = has_item_been_found
        print ('The ' + str(self.tile) + ' rotation is ' + str(self.rotation))
        return

place_tile = TileState(tile.current_area[1], 1, tile.current_area[2],
                       tile.current_area[3], tile.current_area[4],
                       tile.current_area[5], False)
