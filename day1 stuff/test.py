import unittest
import day1

class TestDay1(unittest.TestCase):
    def test_rotate(self):
        self.assertEqual(day1.rotate_dial(50, 'r3'), 53)
        self.assertEqual(day1.rotate_dial(50, 'l3'), 47)
        self.assertEqual(day1.rotate_dial(50, 'l51'), 99)
        self.assertEqual(day1.rotate_dial(50, 'r51'), 1)
        self.assertEqual(day1.rotate_dial(0, 'l1'), 99)
        self.assertEqual(day1.rotate_dial(99, 'r1'), 0)

if __name__ == '__main__':
    unittest.main()