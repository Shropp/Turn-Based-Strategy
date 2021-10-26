import constants
from ursina import *

class Building:

    def __init__(self, building_type, tile, player):
        self.building_type = building_type
        self.visual = Entity( # good luck doing that now. woot woot bitch
            model = 'quad',
            texture = constants.building_asset_table[building_type],
            origin = tile.location,
            scale = (constants.tile_scale, constants.tile_scale, constants.z_scale)
        )
        self.owner = player
        self.turns_until_produce = -1

        self.health = constants.building_health_table[building_type]
    
    def build_unit_possible(tile, building_type):
        return not self.tile.is_occupied() or player.gold >= constants.unit_cost_table[building_type]
