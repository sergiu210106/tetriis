import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.numRows = 20
        self.numCols = 10
        self.cellSize = 30
        self.grid = [[0 for j in range(self.numCols)] for i in range(self.numRows)]
        self.colors = Colors.getCellColors()
    def printGrid(self):
        for row in range(self.numRows):
            for col in range(self.numCols):
                print(self.grid[row][col], end = " ")
            print()
            
    def isInside(self, row, col):
        return (row >= 0 and row < self.numRows and col >= 0 and col < self.numCols)
    
    def isEmpty(self, row, col):
        return self.grid[row][col] == 0
    
    def isRowFull(self, row):
        for col in range(self.numCols):
            if self.grid[row][col] == 0:
                return False
        return True
    
    def clearRow(self, row):
        for col in range(self.numCols):
            self.grid[row][col] = 0
    
    def moveRowDown(self, row, numRows):
        for col in range(self.numCols):
            self.grid[row + numRows][col] = self.grid[row][col]
            self.grid[row][col] = 0
    def clearFullRows(self):
        completed = 0
        
        for row in range(self.numRows - 1, 0, -1):
            if self.isRowFull(row):
                self.clearRow(row)
                completed += 1
            elif completed > 0:
                self.moveRowDown(row, completed)
        return completed
        
    def reset(self):
        for row in range(self.numRows):
            for col in range(self.numCols):
                self.grid[row][col] = 0    
            
    def draw(self, screen):
        for row in range(self.numRows):
            for col in range(self.numCols):
                cellValue = self.grid[row][col]
                cellRect = pygame.Rect(col * self.cellSize + 11, row * self.cellSize + 11, self.cellSize - 1, self.cellSize - 1)
                pygame.draw.rect(screen, self.colors[cellValue], cellRect)