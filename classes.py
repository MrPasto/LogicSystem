from pygame import *
from config import *


class Label:
    def __init__(self, text, font_size=50, font='Arial'):
        self.font_size = font_size
        self.text = text
        self.font = font

    def draw_text(self, screen, color, position=(0, 0), cntr_x=False):
        text = self.text.split('/')

        main_font = font.SysFont(self.font, self.font_size)
        for i, t in enumerate(text):
            caption = main_font.render(t, True, color)
            if cntr_x:
                screen.blit(caption, caption.get_rect(center=(WIDTH // 2, position[1] + i * 50)))
            else:
                screen.blit(caption, (position[0], position[1] + i * 50))


class Rectangle:
    def __init__(self, x, y, x_size, y_size, pic=None, relative_cntr_x=False, relative_cntr_y=False):
        self.x = x
        self.y = y

        self.rc_x = relative_cntr_x
        self.rc_y = relative_cntr_y

        if self.rc_x:
            self.x = (WIDTH // 2) + (x - (x_size // 2))
        if self.rc_y:
            self.y = (HEIGHT // 2) - (y + (y_size // 2))
        self.x_size = x_size
        self.y_size = y_size
        self.radius = int((x_size * y_size) * 0.0004)
        self.rect = Rect(self.x, self.y, self.x_size, self.y_size)
        # self.cntr_rect = Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)

        self.picture = pic
        if self.picture:
            self.picture = transform.scale(image.load(self.picture), self.x_size, self.y_size)

    def draw(self, screen, color, color_border=BLACK):
        if self.picture:
            screen.blit(self.picture, (self.rect.x, self.rect.y))
        else:
            draw.rect(screen, color, self.rect, 0, self.radius)
            draw.rect(screen, color_border, self.rect, 10, self.radius)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


class Game1Button(Rectangle):
    def __int__(self, x, y, x_size, y_size, num, ussed, color=YELLOW, pic=None, relative_cntr_x=False,
                relative_cntr_y=False):
        self.ussed = ussed
        self.num = num
        self.color = color
