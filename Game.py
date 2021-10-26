import TileMap
import Player
import PlayerUnit
import constants
import Inventory
from ursina import *

clicked_info_display = None


class Game:
    global b
    colors = [color.red, color.blue, color.yellow, color.green, color.cyan, color.violet, color.lime, color.orange]
    def __init__(self, num_players):
        self.board = TileMap.TileMap(self)
        self.players = []        
        self.action_queue = []
        
        # create players
        for j in range(num_players):
            self.players.append(Player.Player(self, Game.colors[j]))

        #print(color.colors)
        self.current_player = self.players[0]
        print(self.current_player.color.name)
        
    def new_turn(self):
        for curr_player in self.players:
            print('do your turn bitch')
            # have them do shit using mouse input
            # once they do shit add necessary shit to appropriate list




        # randomize orders of each list
        # resolve each list's actions (assuming each is still valid, e.g swordsman could die before resolving his action)
        # add gold to each player
    
    def tile_clicked(self, tile):
        global clicked_info_display
        if clicked_info_display:
            destroy(clicked_info_display)
            clicked_info_display = None

        if tile.player is None:
            player_col = color.white
        else:
            player_col = tile.player.color

        if tile.building is None:
            building = None
            building_col = color.white
        else:
            building = constants.building_string_table[tile.building.building_type]
            building_col = tile.building.player.color

        if tile.temp_unit is None:
            tile_unit = None
            unit_col = color.white
        else:
            tile_unit = constants.unit_string_table[tile.temp_unit.unit_type]
            unit_col = tile.temp_unit.player.color

        def unit_make():
            if tile.unit == None:
                tile.unit = PlayerUnit.PlayerUnit(0, tile, self.current_player)
                tile.temp_unit = tile.unit
            

        clicked_info_display = Inventory.Inventory(tile)
        clicked_info_display.append(constants.tile_string_table[tile.tile_type], color.white, (0, -1), unit_make)
        clicked_info_display.append(player_col.name, player_col, (1, -1), unit_make)
        clicked_info_display.append(building, building_col, (2, -1), unit_make)
        clicked_info_display.append(tile_unit, unit_col, (3, -1), unit_make)

        #clicked_info_dipsplay.append(random.choice(('bag', 'bow_arrow', 'gem', 'orb', 'sword')), color.random_color(), (i, -1))

        