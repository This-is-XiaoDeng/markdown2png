from pygame.surface import Surface
from . import parser
import pygame
from .style import DefaultStyle, Style

pygame.init()

def draw(ast: list, style: Style) -> Surface:
    surface = Surface(get_size(ast, style))
    surface.fill(style.bg_color)
    now_height = 0
    for item in ast:
        if len(item["innerHTML"]) >= 1 and isinstance(item["innerHTML"][0], dict):
            _surface = draw(item["innerHTML"], style)
        elif item["type"] in style.widghts.keys():
            _surface = style.widghts[item["type"]](item)
        else:
            _surface = style.widghts["text"](item)
        surface.blit(_surface, (0, now_height))
        now_height += _surface.get_size()[1]
    return surface  

def get_size(ast: list, style: Style) -> tuple:
    size = [0, 0]
    # print(ast)
    for item in ast:
        if len(item["innerHTML"]) >= 1 and isinstance(item["innerHTML"][0], dict):
            _size = get_size(item["innerHTML"], style)
        elif item["type"] in style.widghts.keys():
            _size = style.widghts[item["type"]](item).get_size()
        else:
            _size = style.widghts["text"](item).get_size()
        size[0] += _size[0]
        size[1] += _size[1]
    return tuple(size)

def markdown2png(markdown: str, output_path: str, style: Style = DefaultStyle()) -> None:
    pygame.image.save(draw(parser.parse(markdown), style), output_path)
    


    
