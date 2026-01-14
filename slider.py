import pygame

class Slider:
    def __init__(self, pos, length, limits, rounding = 0, default_value = 0):
        self.pos = pos
        self.length = length
        self.lower, self.upper = limits
        self.rounding = rounding
        self.value = default_value

        self.bar = pygame.Rect(self.pos, (self.length, 5))
        self.bar.midleft = self.pos

        self.buffer = 30
        self.collision_box = pygame.Rect(self.bar.topleft, (self.bar.width + self.buffer, self.bar.height + self.buffer))
        self.collision_box.center = self.bar.center

        self.handle_pos = (0, 0)
        self.relative_ratio = 0

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()[2]

        if self.collision_box.collidepoint(mouse_pos) and mouse_pressed:
            self.value = self.lower + (mouse_pos[0] - self.pos[0]) / self.length * (self.upper - self.lower)

        self.value = max(self.lower, min(self.upper, self.value))

        self.value = round(self.value, self.rounding)
        self.relative_ratio = (self.value - self.lower) / (self.upper - self.lower)
        self.handle_pos = (self.pos[0] + self.relative_ratio * self.length, self.pos[1])

    def draw(self, surf):
        pygame.draw.rect(surf, 'grey', self.bar)
        pygame.draw.circle(surf, 'black', self.handle_pos, 10)
