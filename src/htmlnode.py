from textnode import TextNode, TextType

class HTMLNode():

    def __init__(self, tag: str=None, value: str=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        html = ""
        if self.props is None:
            return html
        for prop in self.props:
            html += f' {prop}="{self.props[prop]}"'
        return html

    def __repr__(self):
        print(self.tag, self.value, self.children, self.props)
