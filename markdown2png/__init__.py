from pygame.surface import Surface
from . import parser
import pygame
from .style import DefaultStyle, Style

pygame.init()
NEED_NEWLINE = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "br"]

def draw(ast: list, style: Style) -> Surface:
    # print("Start")
    surface = Surface(get_size(ast, style))
    surface.fill(style.bg_color)
    now_pos = [style.margin[0], style.margin[2]]
    newline = False
    line_height = style.margin[2]
    for item in ast:
        # print("ITEM:",item)
        if type(item) == dict:
            if item["type"] in NEED_NEWLINE:
                newline = True
            if has_dict(item["innerHTML"]):
                _surface = draw(item["innerHTML"], style)
            elif item["type"] in style.widghts.keys():
                _surface = style.widghts[item["type"]](item)
            else:
                _surface = style.widghts["text"](item)
        else:
            _surface = style.widghts["text"]({"innerHTML": [str(item)]})

        surface.blit(_surface, now_pos)
        now_pos[0] += _surface.get_size()[0]
        line_height = max(line_height, _surface.get_size()[1])
        if newline:
            now_pos[1] += line_height + style.margin[2] + style.margin[3]
            now_pos[0] = style.margin[0]
            line_height = 0
            newline = False
            # print("nl")
    # print("End")
    return surface  

def has_dict(items: list):
    for item in items:
        if type(item) == dict:
            return True
    else:
        return False

def get_size(ast: list, style: Style) -> tuple:
    size, newline = [0, 5], False
    _size, _size1 = [0, 0], [0, 0]
    for item in ast:
        if type(item) == dict:
            if item["type"] in NEED_NEWLINE:
                newline = True
            if has_dict(item["innerHTML"]):
                _size1 = get_size(item["innerHTML"], style)
            elif item["type"] in style.widghts.keys():
                _size1 = style.widghts[item["type"]](item).get_size()
            else:
                _size1 = style.widghts["text"](item).get_size()
        else:
            _size1 = style.widghts["text"](
                {"innerHTML": [str(item)]}).get_size()

        _size[0] += _size1[0]
        _size[1] = max(_size[1], _size1[1])
        _size1 = (0, 0)
        
        if newline:
            size[0] = max(size[0], _size[0])
            size[1] += _size[1] + style.margin[2] + style.margin[3]
            _size = [0, 0]
            newline = False
            
    size[0] = max(size[0], _size[0])
    size[1] += _size[1] + style.margin[2] + style.margin[3]
    size[0] += style.margin[0] + style.margin[1]
    return tuple(size)

def markdown2png(markdown: str, output_path: str, style: Style = DefaultStyle()) -> None:
    pygame.image.save(draw(parser.parse(markdown), style), output_path)
    


    
