import unittest
import math

from shape_library import Point, sq_distance, is_triangle, Figure, Circle, Triangle


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        c = Circle(5)
        self.assertAlmostEqual(c.area(), math.pi * 25, places=5)
        c_with_center = Circle(5, Point(1, 1))
        self.assertAlmostEqual(c_with_center.area(), math.pi * 25, places=5)
        c_zero = Circle(0)
        self.assertEqual(c_zero.area(), 0.0)

    def test_circle_errors(self):
        with self.assertRaises(ValueError):
            Circle(-1)
        with self.assertRaises(TypeError):
            Circle("five")
        with self.assertRaises(TypeError):
            Circle(5, "not_point")

    def test_triangle_sides_area(self):
        t = Triangle(3, 4, 5)
        self.assertEqual(t.area(), 6.0)
        t_eq = Triangle(5, 5, 5)
        self.assertAlmostEqual(t_eq.area(), 10.825317547305483, places=5)

    def test_triangle_sides_rectangular(self):
        t = Triangle(3, 4, 5)
        self.assertTrue(t.is_rectangular())
        t_non_rect = Triangle(5, 5, 6)
        self.assertFalse(t_non_rect.is_rectangular())

    def test_triangle_points_area(self):
        p1, p2, p3 = Point(0, 0), Point(3, 0), Point(0, 4)
        t = Triangle(p1, p2, p3)
        self.assertEqual(t.area(), 6.0)
        p_eq1, p_eq2, p_eq3 = (
            Point(0, 0),
            Point(5, 0),
            Point(2.5, (5 * math.sqrt(3) / 2)),
        )
        t_eq = Triangle(p_eq1, p_eq2, p_eq3)
        self.assertAlmostEqual(t_eq.area(), 10.825317547305483, places=5)

    def test_triangle_points_rectangular(self):
        p1, p2, p3 = Point(0, 0), Point(3, 0), Point(0, 4)
        t = Triangle(p1, p2, p3)
        self.assertTrue(t.is_rectangular())

    def test_triangle_errors_sides(self):
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)
        with self.assertRaises(ValueError):
            Triangle(3, 4, 0)
        with self.assertRaises(ValueError):
            Triangle(3, 4, -5)
        with self.assertRaises(TypeError):
            Triangle(3, "4", 5)

    def test_triangle_errors_points(self):
        with self.assertRaises(ValueError):
            Triangle(Point(0, 0), Point(1, 0), Point(2, 0))
        with self.assertRaises(TypeError):
            Triangle(Point(0, 0), 3, 4)

    def test_polymorphism(self):
        figures = [Circle(1), Triangle(3, 4, 5)]
        areas = [f.area() for f in figures]
        self.assertAlmostEqual(areas[0], math.pi, places=5)
        self.assertEqual(areas[1], 6.0)

    def test_is_triangle(self):
        self.assertTrue(is_triangle([3, 4, 5]))
        self.assertFalse(is_triangle([1, 2, 3]))
        self.assertFalse(is_triangle([3, 4, 0]))

    def test_sq_distance(self):
        p1, p2 = Point(0, 0), Point(3, 4)
        self.assertEqual(sq_distance(p1, p2), 25)


if __name__ == "__main__":
    unittest.main()
