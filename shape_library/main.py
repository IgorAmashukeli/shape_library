import math
from abc import ABC, abstractmethod

EPS = 1e-9


class Point:
    """Point in 2D space.

    Attributes:
        x (float): x-coordinate
        y (float): y-coordinate
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


def sq_distance(point_1, point_2):
    """Return squared Euclidean distance between two points.

    Args:
        point_1 (Point): first point
        point_2 (Point): second point

    Returns:
        float: squared distance (dx**2 + dy**2)
    """
    return (point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2


def is_triangle(sides, eps: float = EPS):
    """Check whether three lengths or three Points form a non-degenerate triangle.

    This function accepts either:
      * list with 3 float objects.

    The check uses triangle inequalities with protection against nearly-degenerate
    triangles by rejecting cases where a + b ≈ c (within eps).

    Args:
        sides: float|int instances.
        eps (float): tolerance for considering sums 'close' (default EPS).

    Returns:
        bool: True if the values/points form a valid (non-degenerate) triangle.
    """
    a_len = float(sides[0])
    b_len = float(sides[1])
    c_len = float(sides[2])

    cond1 = (a_len + b_len > c_len) and (
        not math.isclose(a_len + b_len, c_len, rel_tol=eps, abs_tol=eps)
    )
    cond2 = (a_len + c_len > b_len) and (
        not math.isclose(a_len + c_len, b_len, rel_tol=eps, abs_tol=eps)
    )
    cond3 = (b_len + c_len > a_len) and (
        not math.isclose(b_len + c_len, a_len, rel_tol=eps, abs_tol=eps)
    )

    return cond1 and cond2 and cond3


class Figure(ABC):
    """Abstract base class for geometric figures."""

    @abstractmethod
    def area(self):
        """Return area of the figure (float)."""
        pass


class Circle(Figure):
    """Circle defined by center Point and radius."""

    def __init__(self, radius, center=Point(0, 0)):
        """Create a circle.

        Args:
            radius (int|float): radius (non-negative number)
            center (Point): center point


        Raises:
            TypeError: if center is not Point or radius not numeric
            ValueError: if radius is negative
        """
        if not isinstance(center, Point):
            raise TypeError("center must be a Point")
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be an int/float")
        if radius < 0:
            raise ValueError("radius must be non-negative")
        self.radius = float(radius)
        self.center = center

    def area(self):
        """Return circle area (float)."""
        return math.pi * (self.radius**2)


class Triangle(Figure):
    """Triangle defined by three Point objects."""

    def __init__(self, x_1, x_2, x_3):
        """Create a triangle from three Points.

        Args:
            x_1, x_2, x_3 (Point or (int|float)): triangle vertices

        Raises:
            TypeError: if any argument is not a Point/(int|float)
            ValueError: if points do not form a valid (non-degenerate) triangle
        """
        if isinstance(x_1, Point) and isinstance(x_2, Point) and isinstance(x_3, Point):

            self.sq_sides = [
                sq_distance(x_1, x_2),
                sq_distance(x_2, x_3),
                sq_distance(x_3, x_1),
            ]
            self.sides = [math.sqrt(x) for x in self.sq_sides]
        elif (
            isinstance(x_1, (int, float))
            and isinstance(x_2, (int, float))
            and isinstance(x_3, (int, float))
        ):
            if (x_1 <= 0) or (x_2 <= 0) or (x_3 <= 0):
                raise ValueError("all sides should be positive")
            self.sides = [float(x_1), float(x_2), float(x_3)]
            self.sq_sides = [x**2 for x in self.sides]
        else:
            raise TypeError("each point must be a Point or (int|float)")

        if not is_triangle(self.sides):
            raise ValueError("points don't form a valid (non-degenerate) triangle")

    def is_rectangular(self, eps: float = EPS):
        """Return True if the triangle is (approximately) right-angled.

        The check uses squared sides to avoid unnecessary sqrt operations.

        Args:
            eps (float): tolerance for numerical comparison.

        Returns:
            bool: True if right-angled (within eps), False otherwise.
        """
        a2, b2, c2 = sorted(self.sq_sides)
        return math.isclose(a2 + b2, c2, rel_tol=eps, abs_tol=eps)

    def area(self):
        """Return triangle area.

        For right triangles uses 0.5 * cathetus1 * cathetus2,
        otherwise uses Heron's formula.
        """
        if self.is_rectangular():
            a, b, c = sorted(self.sides)
            return a * b / 2.0

        p = sum(self.sides) / 2.0
        return math.sqrt(
            p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])
        )
