from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        texts = old_node.text.split(delimiter)
        if len(texts) % 2 == 0:
            raise Exception("Invalid text type")
        for i in range(len(texts)):
            if texts[i] == "":
                continue
            if i % 2 == 0:
                new_node = TextNode(texts[i], TextType.TEXT)
                new_nodes.append(new_node)
            else:
                new_node = TextNode(texts[i], text_type)
                new_nodes.append(new_node)
    return new_nodes
