from pygame.surface import Surface
import pygame
import os.path

path = os.path.dirname(os.path.abspath(__file__))
BG_COLOR = (255,255,255)

class Style:
    def __init__(self) -> None:
        self.widghts: dict = {}
        self.bg_color: tuple = BG_COLOR
        # Left, Right, Top, Buttom
        self.margin: tuple[int] = (5, 5, 5, 5)

class DefaultStyle(Style):
    def __init__(self) -> None:
        super().__init__()
        self.widghts: dict = {
            "text": text,
            "a": a,
            "p": text,
            "code": code
        }
        for i in range(1, 7):
            self.widghts[f"h{i}"] = eval(f"lambda data: head({i}, data)")

def code(data: dict) -> Surface:
    # print(data)
    text = pygame.font.Font(
        os.path.join(path, "font/sarasa-fixed-cl-regular.ttf"), 20).render(
            "".join(data["innerHTML"]), True, (255, 0, 51), (204, 204, 204))
    surface = Surface((text.get_size()[0], text.get_size()[1]))
    surface.fill(BG_COLOR)
    surface.blit(text, (0, 0))
    return surface

def text(data: dict) -> Surface:
    # print(data)
    text = pygame.font.Font(
        os.path.join(path, "font/sarasa-fixed-cl-regular.ttf"), 20).render(
            "".join(data["innerHTML"]), True, (0, 0, 0))
    surface = Surface((text.get_size()[0], text.get_size()[1]))
    surface.fill(BG_COLOR)
    surface.blit(text, (0, 0))
    return surface

def a(data: dict) -> Surface:
    font = pygame.font.Font(os.path.join(path, "font/sarasa-fixed-cl-regular.ttf"), 20)
    url = font.render(f' ({str(data.get("href"))})', True, (0, 153, 153))
    text = font.render("".join(data["innerHTML"]), True, (0, 153, 255))
    text_size = text.get_size()
    url_size = url.get_size()
    # print(text_size)
    surface = Surface((text_size[0] + url_size[0], text_size[1]))
    surface.fill(BG_COLOR)
    surface.blit(text, (0, 0))
    surface.blit(url, (text_size[0], 0))
    return surface
    
    

def head(level: int, data: dict) -> Surface:
    text = pygame.font.Font(
        os.path.join(path, "font/sarasa-fixed-cl-regular.ttf"), 55 - level * 5).render(
            "".join(data["innerHTML"]), True, (0, 0, 0))
    surface = Surface((text.get_size()[0], text.get_size()[1]))
    surface.fill(BG_COLOR)
    surface.blit(text, (0, 0))
    return surface

