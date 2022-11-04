import pygame

class Button:
    #Constructor
    def __init__(self, pos_x, pos_y, width, height):
        self.rect = pygame.Rect(pos_x, pos_y, width, height)
        self.rect.center = (pos_x, pos_y)

    #Drawing button
    def draw(self, surface, color, thickness, corner, font, text_size, text_color, text):
        #drawing button outline
        pygame.draw.rect(surface, color, self.rect, thickness, corner)

        #text for button
        button_font = pygame.font.SysFont(font, text_size)
        text_width, text_height = button_font.size(text)

        button_name = button_font.render(text, True, text_color)

        text_x = self.rect.x + ((self.rect.width - text_width) / 2)
        text_y = self.rect.y + ((self.rect.height - text_height) / 2)

        #drawing the button and button text
        surface.blit(button_name, (text_x, text_y))

import pygame

class Button:
    #Constructor
    def __init__(self, pos_x, pos_y, width, height):
        self.rect = pygame.Rect(pos_x, pos_y, width, height)
        self.rect.center = (pos_x, pos_y)

    #Drawing button
    def draw(self, surface, color, thickness, corner, font, text_size, text_color, text):
        #drawing button outline
        pygame.draw.rect(surface, color, self.rect, thickness, corner)

        #text for button
        button_font = pygame.font.SysFont(font, text_size)
        text_width, text_height = button_font.size(text)

        button_name = button_font.render(text, True, text_color)

        text_x = self.rect.x + ((self.rect.width - text_width) / 2)
        text_y = self.rect.y + ((self.rect.height - text_height) / 2)

        #drawing the button and button text
        surface.blit(button_name, (text_x, text_y))
