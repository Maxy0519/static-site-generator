import unittest
from leafnode import LeafNode
from parentnode import ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_nested_parent(self):
        child_node1 = LeafNode("i", "child 1")
        child_node2 = LeafNode("span", "child 2")
        parent_node1 = ParentNode("b", [child_node1])
        parent_node2 = ParentNode("div", [child_node2])
        parent_node = ParentNode("p", [parent_node1, parent_node2])
        self.assertEqual(parent_node.to_html(), "<p><b><i>child 1</i></b><div><span>child 2</span></div></p>")

if __name__ == "__main__":
    unittest.main()
