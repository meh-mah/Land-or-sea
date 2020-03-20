from collections import namedtuple
from abc import abstractmethod, ABC


class Shape(ABC):
    """
    Abstract class of shape
    Attributes:
        point (namedtuple): Python namedtuple to represent (x, y) coordinate of a point
    """

    def __init__(self):
        ABC.__init__(self)
        self.point = namedtuple('Point', ['x', 'y'])

    def __repr__(self):
        return self.__str__()

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def width(self):
        pass

    @abstractmethod
    def height(self):
        pass

    @abstractmethod
    def partially_intersect(self, other):
        pass

    @abstractmethod
    def compare(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def __gt__(self, other):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __and__(self, other):
        pass


class Rectangle(Shape):
    """
    Represent a rectangle shape
    Args:
        points (list): A list contain 4 digit corresponding to rectangles min (bottom left) and max (upper right) points.
        first 2 value is x and y of the min point. Values at position 3 and 4 corresponds to x and y of the max point
    Attributes:
        min_point (namedtuple): Python namedtuple to represent (x, y) coordinate of the  min point (bottom left)
        max_point (namedtuple): Python namedtuple to represent (x, y) coordinate of the  max point (upper right)
    Raises:
        ValueError: if number of (x, y) points is not equal 2 OR
        (if x value of min point>= x value of max point OR y value of min point>= y value of max point)
    """

    def __init__(self, points):
        if len(points) != 4:
            raise ValueError(f"Requires 4 values as min/max coordinates but received {points}")
        x1, y1, x2, y2 = points
        if x1 >= x2 or y1 >= y2:
            raise ValueError(f'Coordinates {points} are invalid')
        Shape.__init__(self)
        self.min_point = self.point(x1, y1)
        self.max_point = self.point(x2, y2)

    @property
    def width(self):
        """
        Returns:
            float: width of the rectangle

        """
        return self.max_point.x - self.min_point.x

    @property
    def height(self):
        """
        Returns:
            float: height of the rectangle
        """
        return self.max_point.y - self.min_point.y

    @property
    def area(self):
        """
        Returns:
            float: area of the rectangle

        """
        return self.height * self.width

    def __lt__(self, other):
        """
        Returns True if this object is completely inside the other rectangle
        Args:
            other (Rectangle): The other Rectangle object to do comparison

        Returns:
            bool: True if this object is completely inside the other rectangle.

        """
        if other.min_point.x < self.min_point.x < self.max_point.x < other.max_point.x and \
                other.min_point.y < self.min_point.y < self.max_point.y < other.max_point.y:
            return True
        else:
            return False

    def __gt__(self, other):
        """
        Returns True if the other rectangle is completely inside this object
        Args:
            other (Rectangle): The other Rectangle object to do comparison
        Returns:
            bool: True if the other rectangle is completely inside this object

        """
        if self.min_point.x < other.min_point.x < other.max_point.x < self.max_point.x and \
                self.min_point.y < other.min_point.y < other.max_point.y < self.max_point.y:
            return True
        else:
            return False

    def __eq__(self, other):
        """
        Returns True of this object and the other rectangle have exactly same min and max coordination
        Args:
            other (Rectangle): The other Rectangle object to do comparison

        Returns:
            bool: True if two rectangle are identical

        """
        if self.min_point.x == other.min_point.x and other.max_point.x == self.max_point.x and \
                self.min_point.y == other.min_point.y and other.max_point.y == self.max_point.y:
            return True
        else:
            return False

    def partially_intersect(self, other):
        """
        Returns true if two rectangles overlap with each other partially.
        If a rectangle is fully inside the other one
        AND NOT sharing any boundary we do not consider them as intersecting with each other
        Args:
            other (Rectangle): The other Rectangle object to do comparison

        Returns:
            bool: True if these rectangles intersect

        Notes:
            you can use & operation to call this function

        """
        if self > other or self < other:
            return False
        if self.min_point.x > other.max_point.x or self.max_point.x < other.min_point.x:
            return False
        if self.min_point.y > other.max_point.y or self.max_point.y < other.min_point.y:
            return False
        return True

    __and__ = partially_intersect

    def compare(self, other):
        """
        Comparing two Rectangle objects to identify their position corresponding to each other.
        A rectangle can be inside or outside the other one. They can be identical. They may intersect.
        Or they have not related to each other
        Args:
            other (Rectangle): The other Rectangle object to do comparison

        Returns:
            str: position of this rectangle compare to the other rectangle.
            return value can be one of:
            inside
            outside
            equal
            intersecting
            same level

        """
        if self < other:
            return 'inside'
        if self > other:
            return 'outside'
        if self == other:
            return 'identical'
        if self & other:
            return "intersecting"
        else:
            return 'disjoint'

    def __str__(self):
        return f"min({self.min_point.x},{self.min_point.y}) max({self.max_point.x},{self.max_point.y})"
