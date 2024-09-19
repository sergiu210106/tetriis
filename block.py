from colors import Colors
from position import Position
import pygame
class Block:
    def __init__(self) :
        self.id = id
        self.cells = {} # dict
        self.cellSize = 30
        self.rotationState = 0
        self.colors = Colors.getCellColors()
        self.rowOffset = 0
        self.colOffset = 0
        
    def draw(self, screen, offsetX, offsetY):
        tiles = self.getCellPositions()
        for tile in tiles:
            tileRect = pygame.Rect(tile.col * self.cellSize + offsetX, 
                                   tile.row * self.cellSize + offsetY,
                                   self.cellSize - 1,
                                   self.cellSize - 1)
            pygame.draw.rect(screen, self.colors[self.id], tileRect)
    def move(self, rows, columns):
        self.rowOffset += rows
        self.colOffset += columns
    
    def getCellPositions(self):
        tiles = self.cells[self.rotationState]
        movedTiles = []
        
        for position in tiles:
            position = Position(position.row + self.rowOffset, position.col + self.colOffset)
            movedTiles.append(position)
        return movedTiles
    def rotate(self):
        self.rotationState += 1
        if self.rotationState == len(self.cells):
            self.rotationState = 0

    def undoRotation(self):
        self.rotationState -= 1
        if self.rotationState == -1:
            self.rotationState = len(self.cells) - 1
