import pygame


class Creature(pygame.sprite.Sprite):
    def __init__(self, x0, y0, width, length, color, speed = 1):
        pygame.sprite.Sprite.__init__(self)
        sf = pygame.Surface((width, length))
        sf.fill(color)
        self.image = sf
        self.rect = self.image.get_rect(center = (x0, y0))
        self.speed = speed
        self.width = width
        self.length = length

    def update_left(self, *args) -> None:
        if self.rect.centerx > args[0]:
            self.rect.centerx -= self.speed
        if self.rect.centery > args[1]:
            self.rect.centery -= self.speed

    def update_right(self, *args) -> None:
        if self.rect.centerx < args[0]:
            self.rect.centerx += self.speed
        if self.rect.centery < args[1]:
            self.rect.centery += self.speed

    def update_top(self, *args) -> None:
        if self.rect.centery > args[1]:
            self.rect.centery -= self.speed

    def update_dawn(self, *args) -> None:
        if self.rect.centery < args[1]:
            self.rect.centery += self.speed

    def follow_the_route(self, l: list) -> None:
        pass

