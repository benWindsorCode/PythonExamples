import unittest
from unittest.mock import Mock
from unittest.mock import patch

class DummyClass():
    def func(self):
        return "hello"

# Run in doom emacs with 'SPC-m-t-F'
class DummyClassTest(unittest.TestCase):
    def test_func(self):
        obj = DummyClass()
        obj.func = Mock(return_value="world")

        out = obj.func()
        self.assertEqual(out, "world")

    @patch.object(DummyClass, 'func')
    def test_func_2(self, mock_method):
        DummyClass.func()
        mock_method.assert_called_once()

if __name__ == '__main__':
    unittest.main()
