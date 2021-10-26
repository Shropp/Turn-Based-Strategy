import constants
import Tile

class TileMap:
    
    def __init__(self, game):
        self.tile_map = [[] for _ in range(41)]
        self.game = game

        for x in range(41):
            for y in range(41):
                self.tile_map[y].append(Tile.Tile(x, y, self, game))

    def get(self, x, y):
        return self.tile_map[y][x]
