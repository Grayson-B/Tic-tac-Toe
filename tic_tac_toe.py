import pygame
from pygame.locals import *
pygame.init()
pygame.font.init()

font = pygame.font.SysFont("Courier New", 40)

running = True

window_size = (450,500)


screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Tic Tac Toe")
screen.fill("brown")

class TicTacToe():

    def __init__(self,Table_size):
        self.table_size = Table_size
        self.cell_size = Table_size // 3
    

        self.table_space = 20

        self.player = "X"
        self.winner = None
        self.taking_move = True
        self.running = True
        self.table = []
        for col in range(3):
            self.table.append([])
            for row in range(3):
                self.table[col].append("-")
        
        self.background_color = (255,174,66)
        self.table_color = (50,50,50)
        self.line_color = (190,0,10)
        self.instructions_color = (17,53,165)
        self.game_over_bg_color = (255,179,1)
        self.game_over_color = (255,179,1)
        self.font = pygame.font.SysFont("Courier New", 35)
        self.FPS = pygame.time.Clock()
    
    def _draw_table(self):
        tb_space_point = (self.table_space, self.table_size - self.table_space)
        cell_space_point = (self.cell_size, self.cell_size * 2)
        r1 = pygame.draw.line(screen, self.table_color,[tb_space_point[0], cell_space_point[0]], [tb_space_point[1], cell_space_point[0]], 8)
        c1 = pygame.draw.line(screen, self.table_color,[tb_space_point[0], cell_space_point[0]], [tb_space_point[0], cell_space_point[1]], 8)
        r2 = pygame.draw.line(screen, self.table_color,[tb_space_point[0], cell_space_point[1]], [tb_space_point[1], cell_space_point[1]], 8)
        c2 = pygame.draw.line(screen, self.table_color,[tb_space_point[1], cell_space_point[0]], [tb_space_point[1], cell_space_point[1]], 8)

    def _change_player(self):
        self.player = "O" if self.player == "X" else "X"

    def _move(self, pos):
        try:
            x, y = pos[0] // self.cell_size, pos[1] // self.cell_size
            if self.table[x][y] == "-"
            

pygame.display.update()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False





pygame.quit()