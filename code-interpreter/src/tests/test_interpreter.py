import unittest
from interpreter.executor import Executor
from interpreter.error_parser import ErrorParser

class TestInterpreter(unittest.TestCase):

    def setUp(self):
        self.executor = Executor()
        self.error_parser = ErrorParser()

    def test_execute_valid_code(self):
        code = "print('Hello, World!')"
        output = self.executor.execute(code)
        self.assertEqual(output, "Hello, World!\n")
        self.assertEqual(self.executor.message, "Code executed with no warnings and errors.")

    def test_execute_invalid_code(self):
        code = "print('Hello, World!'"
        output = self.executor.execute(code)
        error_message = self.error_parser.parse(output)
        self.assertIn("You missed a closing parenthesis", error_message)

if __name__ == '__main__':
    unittest.main()