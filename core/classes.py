from pygame import *
from core.config import *


class Label:
    def __init__(self, text=None, rect_=None, font_size=50, font_='Arial', italiano=False):
        self.rect_ = rect_
        self.font_size = font_size
        self.text = text
        self.font = font_
        self.italiano = italiano

    def draw_text(self, screen, color_, position=(0, 0), cntr_x=False, text_=None):
        text: str = ''
        if self.text:
            text = self.text.split('//')
        if text_:
            text = text_.split('//')

        main_font = font.SysFont(self.font, self.font_size, italic=self.italiano)
        for i, t in enumerate(text):
            caption = main_font.render(t, True, color_)

            if self.rect_:
                if cntr_x:
                    pos = caption.get_rect(center=(self.rect_.x + self.rect_.x_size // 2,
                                                   (self.rect_.y + self.rect_.y_size // (2 * len(text))) + i * 50))
                else:
                    pos = (self.rect_.x + 20, self.rect_.y + i * 50 + 15)
            else:
                if cntr_x:
                    pos = caption.get_rect(center=(WIDTH // 2 + position[0], position[1] + i * 50))
                else:
                    pos = (position[0], position[1] + i * 50)
            screen.blit(caption, pos)


class Rectangle:
    def __init__(self, x, y, x_size, y_size, pic=None, color_b=YELLOW, is_radius=True, is_found=False,
                 relative_cntr_x=False, relative_cntr_y=False):
        self.x = x
        self.y = y

        self.is_found = is_found

        self.color_b = color_b

        self.rc_x = relative_cntr_x
        self.rc_y = relative_cntr_y

        if self.rc_x:
            self.x = (WIDTH // 2) + (x - (x_size // 2))
        if self.rc_y:
            self.y = (HEIGHT // 2) - (y + (y_size // 2))
        self.x_size = x_size
        self.y_size = y_size
        self.radius = 0
        if is_radius:
            self.radius = int((x_size * y_size) * 0.0004)
        self.rect = Rect(self.x, self.y, self.x_size, self.y_size)
        # self.cntr_rect = Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)

        self.picture = pic
        if self.picture:
            self.picture = transform.scale(image.load(self.picture), self.x_size, self.y_size)

    def draw(self, screen, color_, color_border=BLACK):
        if self.picture:
            screen.blit(self.picture, (self.rect.x, self.rect.y))
        else:
            draw.rect(screen, color_, self.rect, 0, self.radius)
            draw.rect(screen, color_border, self.rect, 10, self.radius)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)


class GameButton(Rectangle):
    def __int__(self, x, y, x_size, y_size, num, is_used, is_pressed=False, color_=YELLOW, pic=None,
                relative_cntr_x=False, relative_cntr_y=False):
        self.is_used = is_used
        self.is_pressed = is_pressed
        self.num = num
        self.color = color_
