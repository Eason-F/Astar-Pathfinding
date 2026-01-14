import pygame

class Slider:
    def __init__(self, pos, length, limits, rounding = 0, default_value = 0):
        self.pos = pos
        self.length = length
        self.limits = limits
        self.rounding = rounding

        self.bar = pygame.Rect(self.pos, (self.pos[0] + self.length, self.pos[1] + 20))

        self.value = default_value

    def update(self):
        pass

    def draw(self, surf):
        pygame.draw.rect(surf, 'grey', self.bar)
