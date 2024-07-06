import pygame
import random
pygame.init()

class DrawInformation: 
    BLACK = 0,0,0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE

    SIDE_PAD = 100
    TOP_PAD = 150

    def __init__(self, width, height, lst): 
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height)) 
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def self_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        #block width determined according to how many items
        self.block_width = round(self.width - self.SIDE_PAD) / len(lst)
        #Find out the range of values
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2
        