import unittest

from textnode import TextNode, TextTypes

from converter import text_node_to_html_node


class TestConverter(unittest.TestCase):
    def test_exceptions(self):
        print("\n--- Testing Converter: Exceptions ---\n")
        print("Testing inexistent text_type")
        with self.assertRaises(KeyError) as cm:
            text_node_to_html_node(TextNode("text", None))
        self.assertTrue(cm.exception.__class__ is KeyError)

        print("Testing invalid text_type")

        with self.assertRaises(KeyError) as cm:
            text_node_to_html_node(TextNode("text", "images"))
        self.assertTrue(cm.exception.__class__ is KeyError)

        print("\n--- END OF Testing Converter: Exceptions ---\n")

    def test_eq(self):
        print("\n--- Testing Converter: all text_types cases ---\n")
        text_node = TextNode("Click me!", "link", "https://boot.dev")

        print(f"Text node: {repr(text_node)}")

        html_node = text_node_to_html_node(text_node)

        print(f"HTML (converted) node: {repr(html_node)}")

        html_string = html_node.to_html()

        self.assertEqual(html_string, '<a href="https://boot.dev">Click me!</a>')

        html_strings_dict = {}

        for text_type in TextTypes:
            html_strings_dict[text_type.name] = text_node_to_html_node(
                TextNode(
                    "this is an example",
                    text_type.name,
                    "public/image.jpg" if text_type.name == "image" else None,
                )
            ).to_html()

        for k, current in html_strings_dict.items():
            print(f"Testing for text type: {k}")
            match k:
                case "text":
                    self.assertEqual(current, "this is an example")
                case "bold":
                    self.assertEqual(current, "<b>this is an example</b>")
                case "italic":
                    self.assertEqual(current, "<i>this is an example</i>")
                case "code":
                    self.assertEqual(current, "<code>this is an example</code>")
                case "image":
                    self.assertEqual(
                        current,
                        '<img src="public/image.jpg" alt="this is an example"></img>',
                    )

        print("\n--- END OF Testing Converter ---\n")
