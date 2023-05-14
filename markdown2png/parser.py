import xml.dom.minidom
import marko

def markdown2html(markdown: str) -> str:
    return f"<div>{marko.convert(markdown)}</div>".replace("\n", "")

def parse_dom(nodes: list) -> list:
    ast, item = [], {}
    for node in nodes:
        item["type"] = node.nodeName
        if node.attributes != None:
            for attr in node.attributes.items():
                item[attr[0]] = attr[1]
        item["innerHTML"] = parse_dom(node.childNodes)
        if node.nodeType == node.TEXT_NODE:
            item = node.data
        ast.append(item)
        item = {}
    return ast

def parseHTML(html: str) -> list:
    dom = xml.dom.minidom.parseString(html)
    return parse_dom(dom.childNodes)

def parse(markdown: str) -> list:
    return parseHTML(markdown2html(markdown))

     
