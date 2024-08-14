import pygame as p
p.init()


class Button:  # button class
    def __init__(self, text, color, location, screen):
        self.size = 120  # length of each button
        self.text = text  # text on the button
        self.screen = screen
        self.color = color  # color of the button
        self.location = location  # number of buttons preceding and including this button
        self.font = p.font.SysFont('Times New Roman', 25)  # font of the text on each button
        self.panel = p.draw.rect(self.screen, 'gray', (0, 600, 0, 50))  # button panel
        self.template = p.Rect(0, 0, self.size, 50)  # template for all buttons

    def drawButton(self):  # draws buttons
        but = self.template.clamp(self.panel).move(self.location * self.size + 60, 25)  #creates the button
        p.draw.rect(self.screen, self.color, but)  # draws button
        line = self.font.render(self.text, True, 'black')  # creates text
        self.screen.blit(line, but.move(10, 0))  # draws text
        return but  # returns the button
