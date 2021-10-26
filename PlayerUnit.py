import constants
from ursina import *

class PlayerUnit:
    def __init__(self, unit_type, tile, player):
        self.unit_type = unit_type
        self.tile = tile
        self.player = player
        
        self.health = constants.unit_health_table[unit_type]
        self.move_tiles = []
        self.attack_tiles = []
        self.prev_tile = None
        self.moves = constants.unit_movement_table[unit_type]
        self.action_queue = []
        self.attacking = False
        self.sieging = False

        self.unit_sprite = Entity( # good luck doing that now. woot woot bitch
            model = 'quad',
            texture = constants.unit_asset_table[unit_type],
            position = tile.visual.position + (-.5 * constants.tile_scale, 0.5 * constants.tile_scale,-.01),
            origin = (-.5,.5),
            scale = (constants.tile_scale / 2, constants.tile_scale / 2, constants.z_scale),
            color = player.color
        )

    def siege_possible(self, victim_tile):
        return victim_tile in self.attack_tiles and victim_tile.building and \
                self.player != victim_tile.player

    def attack_possible(self, victim_tile):
        return victim_tile in self.attack_tiles and victim_tile.unit and \
                self.player != victim_tile.player 

    def move_possible(self, dest_tile):
        return dest_tile in self.move_tiles and not dest_tile.is_occupied()

    def build_possible(self, dest_tile, building_type):
        return dest_tile in self.attack_tiles and not dest_tile.is_occupied() and \
                self.player.gold >= constants.unit_cost_table[building_type]
            
    def move_pathfind(self, tilemap):
        self.move_tiles = []

        process_nodes = [(self.tile, self.moves)]
        used_nodes = dict()

        while len(process_nodes):
            curr_node = process_nodes.pop(0)
            if curr_node[0].location in used_nodes and used_nodes[curr_node[0].location] <= curr_node[1]:
                continue
            else:
                used_nodes[curr_node[0].location] = curr_node[1]

            if curr_node[1] >= 0 and not curr_node[0].is_occupied():
                self.move_tiles.append(curr_node[0])

            curr_x = curr_node[0].location[0]
            curr_y = curr_node[0].location[1]

            dist = curr_node[1] - constants.tile_movement_cost[curr_node[0].tile_type]

            if curr_x - 1 != 0 and (not tilemap.tile_map.get(curr_x - 1, curr_y).building) and curr_node[1] > 0:
                process_nodes.append((tilemap.tile_map.get(curr_x - 1, curr_y), dist))
            if curr_x + 1 != constants.map_width and (not tilemap.tile_map.get(curr_x + 1, curr_y).building) and curr_node[1] > 0:
                process_nodes.append((tilemap.tile_map.get(curr_x + 1, curr_y), dist))
            if curr_y - 1 != 0 and (not tilemap.tile_map.get(curr_x, curr_y - 1).building) and curr_node[1] > 0:
                process_nodes.append((tilemap.tile_map.get(curr_x, curr_y - 1), dist))
            if curr_y + 1 != constants.map_height and (not tilemap.tile_map.get(curr_x, curr_y + 1).building) and curr_node[1] > 0:
                process_nodes.append((tilemap.tile_map.get(curr_x, curr_y + 1), dist))

    def attack_pathfind(self, tilemap):
        self.attack_tiles = []

        process_nodes = [(self.tile, constants.unit_range_table[self.unit_type])]
        used_nodes = dict()

        while len(process_nodes):
            curr_node = process_nodes.pop(0)
            if curr_node[0].location in used_nodes and used_nodes[curr_node[0].location] <= curr_node[1]:
                continue
            else:
                used_nodes[curr_node[0].location] = curr_node[1]

            if curr_node[1] >= 0 and curr_node[0].is_occupied() and curr_node[0].player != self.player:
                self.attack_tiles.append(curr_node[0])

            curr_x = curr_node[0].location[0]
            curr_y = curr_node[0].location[0]

            dist = curr_node[1] - constants.tile_range_cost[curr_node[0].tile_type]

            if curr_x - 1 != 0 and curr_node[1] > 0:
                process_nodes.append((tilemap.tile_map.get(curr_x - 1, curr_y), dist))
            if curr_x + 1 != constants.map_width and curr_node[1] > 0:
                process_nodes.append((tilemap.tile_map.get(curr_x + 1, curr_y), dist))
            if curr_y - 1 != 0 and curr_node[1] > 0:
                process_nodes.append((tilemap.tile_map.get(curr_x, curr_y - 1), dist))
            if curr_y + 1 != constants.map_height and curr_node[1] > 0:
                process_nodes.append((tilemap.tile_map.get(curr_x, curr_y + 1), dist))