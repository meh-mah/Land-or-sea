import unittest

from shapes import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        # test cases
        self.Rectangle1 = Rectangle([1.5, 2, 4.5, 6.2])
        self.Rectangle2 = Rectangle([1.5, 6.2, 4, 7])
        self.Rectangle3 = Rectangle([-1, -1, 2.5, 2])
        self.Rectangle4 = Rectangle([4.5, 6.2, 5, 7])
        self.Rectangle5 = Rectangle([1.5, 2, 4.5, 6.2])
        self.Rectangle6 = Rectangle([-1, 2, 1.5, 3])
        self.Rectangle7 = Rectangle([-1, -3, 4.5, 2])
        self.Rectangle8 = Rectangle([4.5, 2, 6.5, 3])
        self.Rectangle9 = Rectangle([4.6, 2, 6.5, 4])
        self.Rectangle10 = Rectangle([2, 2.5, 4, 6])
        self.Rectangle11 = Rectangle([1.5, 2, 3.5, 5.2])
        self.Rectangle12 = Rectangle([2, 3, 4.5, 6.2])
        self.Rectangle13 = Rectangle([1.5, 2, 5, 7])
        self.Rectangle14 = Rectangle([1, 1, 4.5, 6.2])

    def test_width(self):
        """
        Check if width calculation is correct

        """
        self.assertEqual(self.Rectangle1.width, 3)

    def test_height(self):
        """
        Check if height calculation is correct
        """
        self.assertEqual(self.Rectangle1.height, 4.2)

    def test_area(self):
        """
        Check if area calculation is correct
        """
        self.assertAlmostEqual(self.Rectangle1.area, 12.6)

    def test_is_intersect(self):
        """
        Check if __and__ implemented correctly to find partially intersecting rectangles
         to find intersecting rectangles
        """
        # partially intersecting
        self.assertTrue(self.Rectangle1 & self.Rectangle1)
        self.assertTrue(self.Rectangle1 & self.Rectangle2)
        self.assertTrue(self.Rectangle1 & self.Rectangle3)
        self.assertTrue(self.Rectangle1 & self.Rectangle4)
        self.assertTrue(self.Rectangle1 & self.Rectangle5)
        self.assertTrue(self.Rectangle1 & self.Rectangle6)
        self.assertTrue(self.Rectangle1 & self.Rectangle7)
        self.assertTrue(self.Rectangle1 & self.Rectangle8)

        # one fully inside the other one but sharing same boundary
        self.assertTrue(self.Rectangle1 & self.Rectangle11)
        self.assertTrue(self.Rectangle1 & self.Rectangle12)

        # One is fully inside the other one
        self.assertFalse(self.Rectangle1 & self.Rectangle10)

        # Fully disjoint
        self.assertFalse(self.Rectangle1 & self.Rectangle9)

    def test_compare(self):
        """
        check __lt__, __gt__, __eq__, and being fully disjoint
        """
        # same coordinates
        self.assertEqual(self.Rectangle1, self.Rectangle1)
        # 1 fully wrapping 10
        self.assertGreater(self.Rectangle1, self.Rectangle10)
        # 10 is fully inside 1
        self.assertLess(self.Rectangle10, self.Rectangle1)
        # Fully disjoint
        self.assertEqual(self.Rectangle1.compare(self.Rectangle9), 'disjoint')
        # fully inside Rectangle1 but sharing same boundary
        self.assertFalse(self.Rectangle11 < self.Rectangle1)
        self.assertFalse(self.Rectangle12 < self.Rectangle1)
        # fully outside Rectangle1 but sharing same boundary
        self.assertFalse(self.Rectangle13 > self.Rectangle1)
        self.assertFalse(self.Rectangle14 > self.Rectangle1)

    def test_exception(self):
        """
        Test if exception raises if given coordinates are NOT valid to shape a rectangle

        """
        # bottom left coordinate must be smaller than top right coordinate
        self.assertRaisesRegex(ValueError, r'Coordinates \[4.6, 2, 4.6, 3\] are invalid', Rectangle, [4.6, 2, 4.6, 3])
        self.assertRaisesRegex(ValueError, r'Coordinates \[4.6, 2, 4.5, 3\] are invalid', Rectangle, [4.6, 2, 4.5, 3])
        self.assertRaisesRegex(ValueError, r'Coordinates \[4.6, 2, 5.5, 2\] are invalid', Rectangle, [4.6, 2, 5.5, 2])
        self.assertRaisesRegex(ValueError, r'Coordinates \[4.6, 2, 5.5, 1.9\] are invalid', Rectangle,
                               [4.6, 2, 5.5, 1.9])
        self.assertRaisesRegex(ValueError, r'Requires 4 values as min/max coordinates but received \[4.6, 2, 5.5\]',
                               Rectangle, [4.6, 2, 5.5])
        self.assertRaisesRegex(ValueError,
                               r'Requires 4 values as min/max coordinates but received \[4.6, 2, 5.5, 5, 3\]',
                               Rectangle, [4.6, 2, 5.5, 5, 3])


if __name__ == '__main__':
    unittest.main()
