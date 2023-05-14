from pygame.surface import Surface
import pygame
import os.path

path = os.path.dirname(os.path.abspath(__file__))
BG_COLOR = (255,255,255)

class Style:
    def __init__(self) -> None:
        self.widghts: dict = {}
        self.bg_color: tuple = BG_COLOR

class DefaultStyle(Style):
    def __init__(self) -> None:
        super().__init__()
        self.widghts: dict = {
            "text": text
        }
        for i in range(1, 7):
            self.widghts[f"h{i}"] = eval(f"lambda data: head({i}, data)")
"""
class H1(Widght):
    def __init__(self) -> None:
        self.font = pygame.font.Font(os.path.join(path, "font/sarasa-fixed-cl-regular.ttf"), 50)
    def get_size(self, data: dict) -> tuple:
        return self.font.render(data["innerHTML"], True, (0, 0, 0)).get_size()
    def draw(self, surface: pygame.Surface, pos: tuple) -> None:
        surface.blit(
            self.font.render()
        )
"""

def text(data: dict) -> Surface:
    text = pygame.font.Font(
        os.path.join(path, "font/sarasa-fixed-cl-regular.ttf"), 20).render(
            "".join(data["innerHTML"]), True, (0, 0, 0))
    surface = Surface((text.get_size()[0] + 10, text.get_size()[1] + 10))
    surface.fill(BG_COLOR)
    surface.blit(text, (5, 5))
    return surface

def head(level: int, data: dict) -> Surface:
    print(level)
    text = pygame.font.Font(
        os.path.join(path, "font/sarasa-fixed-cl-regular.ttf"), 55 - level * 5).render(
            "".join(data["innerHTML"]), True, (0, 0, 0))
    surface = Surface((text.get_size()[0] + 10, text.get_size()[1] + 10))
    surface.fill(BG_COLOR)
    surface.blit(text, (5, 5))
    return surface

