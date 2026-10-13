import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode("a", "Google", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_values(self):
        node = HTMLNode("p", "Hello, world!")
        self.assertEqual(node.value, "Hello, world!")

    def test_children(self):
        node = HTMLNode(children=[HTMLNode("span", "Icon", None, None)])
        node2 = HTMLNode(children=[HTMLNode(None, None, None, None)])
        self.assertNotEqual(node.children[0].tag, node2.children[0].tag)

if __name__ == "__main__":
    unittest.main()
