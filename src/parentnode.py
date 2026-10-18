from htmlnode import HTMLNode


class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node has no tag")
        if self.children == None:
            raise ValueError("Parent node has no children")
        children = ""
        for child in self.children:
            children += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"
    