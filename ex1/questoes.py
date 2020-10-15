import unittest
from unittest import mock
import io
from hello_world import my_functions


class Test101(unittest.TestCase):
    def test_name(self):
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
            my_functions.hello('Monty')
            self.assertEqual('Hello, Monty\n', fake_out.getvalue())

    def test_ask(self):
        with mock.patch('builtins.input', return_value="Python"):
            self.assertEqual('Python', my_functions.ask_for_name())


if __name__ == '__main__':
    unittest.main(verbosity=2)
