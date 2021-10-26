import constants
from ursina import *

hover = Entity( # good luck doing that now. woot woot bitch
            model = 'quad',
            texture = constants.tile_asset_table[5],
            position = (1000,0,.01),
            scale = (constants.tile_scale, constants.tile_scale, constants.z_scale),
        )
highlight = Entity( # good luck doing that now. woot woot bitch
            model = 'quad',
            texture = constants.tile_asset_table[4],
            position = (1000,0,.01),
            scale = (constants.tile_scale, constants.tile_scale, constants.z_scale),
        )        

class Tile:

    def __init__(self, x, y, board, game):
        self.tile_type= constants.tile_type_assignment[y][x]
        self.visual = Entity( # good luck doing that now. woot woot bitch
            model = 'quad',
            texture = constants.tile_asset_table[self.tile_type],
            position = ((x - constants.map_width // 2) * constants.tile_scale, -(y - constants.map_height // 2) * constants.tile_scale, 0),
            # origin = (2 * (x - constants.map_width // 2) * constants.tile_scale, 2 * (y - constants.map_height // 2) * constants.tile_scale, 0),
            scale = (constants.tile_scale, constants.tile_scale, constants.z_scale),
            collider='box',
            on_click = self.mouse_highlight,
            on_mouse_enter = self.mouse_hover
        )
        self.building = None
        self.unit = None
        self.player = None
        self.location = (x, y)
        self.board = board
        self.game = game
        self.temp_unit = None

    def tile_dist(self, tile):
        return abs(self.x + self.y - tile.x - tile.y)

    def is_occupied(self):
        return (self.building or self.unit or not self in self.player.temp_occupied) and not self in self.player.temp_empty

    def occupied_by(self):
        return self.player.color

    def what_type(self):
        return self.tile_type

    def mouse_hover(self):
        #print(self.visual.origin)
        hover.position = self.visual.position + (0,0,-.015)
        hover.texture = constants.tile_asset_table[5]
        #hover.origin += self.visual.origin + hover.origin
    def mouse_highlight(self):
        
        #print(self.visual.origin)
        highlight.position = self.visual.position + (0,0,-.02)
        highlight.texture = constants.tile_asset_table[4]
        #highlight.origin += self.visual.origin + highlight.origin
        self.game.tile_clicked(self)