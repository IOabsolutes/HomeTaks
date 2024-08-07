import unittest
from unittest.mock import patch
from io import StringIO
from main import parser_input, action
from actions import add_contact, change_contact, show_phone, show_all
import actions


class TestAssistantBot(unittest.TestCase):

    def setUp(self):
        actions.storege.clear()

    def test_parser_input(self):
        self.assertEqual(
            parser_input("ADD John 1234567890"), ("add", "John", "1234567890")
        )
        self.assertEqual(parser_input("PHONE Alice"), ("phone", "Alice"))
        self.assertEqual(parser_input("EXIT"), ("exit",))

    def test_add_contact(self):
        add_contact(["John", "1234567890"])
        self.assertEqual(actions.storege, {"John": "1234567890"})

    def test_change_contact(self):
        actions.storege = {"John": "1234567890"}
        change_contact(["John", "9876543210"])
        self.assertEqual(actions.storege, {"John": "9876543210"})

    def test_show_phone(self):
        actions.storege = {"John": "1234567890"}
        with patch("sys.stdout", new=StringIO()) as fake_out:
            show_phone(["John"])
            self.assertIn("The phone number --> 1234567890", fake_out.getvalue())

    def test_show_all(self):
        actions.storege = {"John": "1234567890", "Alice": "9876543210"}
        with patch("sys.stdout", new=StringIO()) as fake_out:
            show_all()
            output = fake_out.getvalue()
            self.assertIn("Name: John; phone: 1234567890", output)
            self.assertIn("Name: Alice; phone: 9876543210", output)

    def test_action(self):
        test_cases = [
            ("add", ["John", "1234567890"], "Contact added."),
            ("phone", ["John"], "The phone number --> 1234567890"),
            ("change", ["John", "9876543210"], "Contact updated."),
            ("hello", [], "How can I help you?"),
            ("invalid", [], "Invalid command"),
        ]

        for command, params, expected_output in test_cases:
            with self.subTest(command=command):
                if command == "phone":
                    actions.storege = {"John": "1234567890"}
                with patch("sys.stdout", new=StringIO()) as fake_out:
                    action(command, *params)
                    self.assertIn(expected_output, fake_out.getvalue())

    @patch(
        "builtins.input",
        side_effect=[
            "ADD John 1234567890",
            "PHONE John",
            "CHANGE John 9876543210",
            "ALL",
            "EXIT",
        ],
    )
    def test_main_flow(self, mock_input):
        import main

        with patch("sys.stdout", new=StringIO()) as fake_out:
            with self.assertRaises(SystemExit):
                main.main()
            output = fake_out.getvalue()
            self.assertIn("Contact added.", output)
            self.assertIn("The phone number --> 1234567890", output)
            self.assertIn("Contact updated.", output)
            self.assertIn("Name: John; phone: 9876543210", output)
            self.assertIn("Good bye!", output)


if __name__ == "__main__":
    unittest.main()
