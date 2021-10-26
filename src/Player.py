import constants

class Player:

    def __init__(self, game, color):
        self.gold = constants.starting_gold
        self.color = color
        self.game = game
        self.actions_per_turn = 10
        self.buildings = []
        self.units = []
        self.temp_occupied = []
        self.temp_empty = []
    
    def queue_move_unit(self, unit, dest_tile):
        if not unit.move_possible(dest_tile):
            return None
        
        if unit.moves == constants.unit_movement_table[unit.unit_type]:
            unit.prev_tile = unit.tile

        if unit.tile in self.temp_occupied:
            self.temp_occupied.remove(unit.tile)
        self.temp_empty.append(unit.tile)

        unit.tile = dest_tile

        self.temp_occupied.append(dest_tile)
        
        for i in units:
            i.pathfind()
        
    def reset_turn(self):        
        for unit in self.units:
            if unit.prev_tile:
                unit.tile = unit.prev_tile
            unit.prev_tile = None

            unit.action_queue = []
        
        

        
    




