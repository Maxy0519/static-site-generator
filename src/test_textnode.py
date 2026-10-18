import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_TextType(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
            node = TextNode("This is a bold node", TextType.BOLD)
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, "b")
            self.assertEqual(html_node.value, "This is a bold node")

    def test_link(self):
                node = TextNode("This is a link node", TextType.LINK, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                html_node = text_node_to_html_node(node)
                self.assertEqual(html_node.tag, "a")
                self.assertEqual(html_node.value, "This is a link node")
                self.assertEqual(html_node.props, {"href": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"})


if __name__ == "__main__":
    unittest.main()
