from math import (
    atan2,
    degrees,
    e,
    exp,
    log,
    sqrt,
    radians,
    tan,
    atan,
    acos,
    cos,
    sin,
    degrees,
)

from typing import Union, Tuple, List, Sequence
from classtools import Verifiers
from matplotlib import pyplot as plt
from matplotlib import patches

# Creating some references
verify_type = Verifiers.verify_type
verify_length = Verifiers.verify_length
verify_indexable = Verifiers.verify_indexable
verify_components_type = Verifiers.verify_components_type

# Senior tasks
"""
Optimización y Rendimiento
Escalabilidad y Diseño de Sistemas
Aprender a hacer clases modulares profesionales
Manejo Avanzado de Errores y Excepciones
Pruebas Automatizadas y Cobertura de Código
Documentación Exhaustiva y Mejora Continua
Conocimiento Profundo del Dominio
"""
# Tasks
"""
1. Add functionallity for classes to not verify at all the types when setting properties (add self._verify: bool).
"""


class Point:
    """Class representating a point in the Euclidean space."""

    def __init__(self, x: Union[int, float], y: Union[int, float], /) -> None:
        """
        Initialize a Point object with coordinates (x, y).

        Args:
            x (int/float): x-coordinate of the point.
            y (int/float): y-coordinate of the point.
        """
        self._x = verify_type(x, (int, float))
        self._y = verify_type(y, (int, float))

    @property
    def x(self) -> Union[int, float]:
        """Return the x-coordinate of the point."""
        return self._x

    @x.setter
    def x(self, value: Union[int, float]) -> None:
        """
        Set the x-coordinate of the point.

        Args:
            value (int | float): New value for the x-coordinate.

        Raises:
            TypeError: If the value is not numeric.
        """
        verify_type(value, (int, float))
        self._x = value

    @property
    def y(self) -> Union[int, float]:
        """Return the y-coordinate of the point."""
        return self._y

    @y.setter
    def y(self, value: int | float) -> None:
        """
        Set the y-coordinate of the point.

        Args:
            value (int | float): New value for the y-coordinate.

        Raises:
            TypeError: If the value is not numeric.
        """
        verify_type(value, (int, float))
        self._y = value

    def __repr__(self) -> str:
        """Return a string representation of the Point object."""
        return f"Point({self.x}, {self.y})"

    def __str__(self) -> str:
        """Return a formatted string of the Point coordinates."""
        return f"({self.x}, {self.y})"

    def __eq__(self, other: object, /) -> bool:
        """
        Compare two Point objects for equality.

        Args:
            other (object): Another object to compare with.

        Returns:
            bool: True if both objects are equal, False otherwise.
        """
        if isinstance(other, (tuple, list)):
            try:
                verify_length(other, 2)
            except:
                return False

            other = Point(*other)

        return self.__dict__ == other.__dict__

    def __add__(
        self,
        other: Union[
            "Point",
            Tuple[Union[int, float], Union[int, float]],
            List[Union[int, float]],
        ],
        /,
    ) -> "Point":
        """
        Return the vector sum of two points.

        Args:
            other (Point | tuple[int | float, int | float] | list[int | float]):
                The other point or tuple/list representing coordinates.

        Returns:
            Point: A new Point object representing the sum of self and other.

        Raises:
            TypeError: If the type of other is not supported.
            IndexError: If other is a tuple/list and its length is not 2.
        """
        verify_type(other, (Point, tuple, list))
        verify_length(other, 2)

        if not isinstance(other, Point):
            other = Point(*other)

        return Point(self.x + other.x, self.y + other.y)

    def __sub__(
        self,
        other: Union[
            "Point",
            Tuple[Union[int, float], Union[int, float]],
            List[Union[int, float]],
        ],
        /,
    ) -> "Point":
        """
        Return the vector difference of two points.

        Args:
            other (Point | tuple[int | float, int | float] | list[int | float]):
                The other point or tuple/list representing coordinates.

        Returns:
            Point: A new Point object representing the difference self - other.

        Raises:
            TypeError: If the type of other is not supported.
            IndexError: If other is a tuple/list and its length is not 2.
        """
        verify_type(other, (Point, tuple, list))
        verify_length(other, 2)

        if not isinstance(other, Point):
            other = Point(*other)

        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: Union[int, float], /) -> "Point":
        """
        Return the scaled point by a scalar.

        Args:
            scalar (int | float): The scalar value to scale the point.

        Returns:
            Point: A new Point object scaled by the scalar.
        """
        return Point(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: Union[int, float], /) -> "Point":
        """
        Return the scaled point by a scalar (scalar * point).

        Args:
            scalar (int | float): The scalar value to scale the point.

        Returns:
            Point: A new Point object scaled by the scalar.
        """
        return self * scalar

    def __truediv__(self, scalar: Union[int, float], /) -> "Point":
        """
        Return the point scaled down by a scalar.

        Args:
            scalar (int | float): The scalar value to divide the point by.

        Returns:
            Point: A new Point object scaled down by the scalar.
        """
        return Point(self.x / scalar, self.y / scalar)

    def __neg__(self) -> "Point":
        """
        Return the negation of the point.

        Returns:
            Point: A new Point object with negated coordinates.
        """
        return Point(-self.x, -self.y)

    def __abs__(self) -> float:
        """
        Return the Euclidean distance of the point from the origin.

        Returns:
            float: The Euclidean distance of the point from the origin.
        """
        return sqrt(self.x**2 + self.y**2)

    def __len__(self) -> int:
        """
        Return the dimension of the point (always 2 for 2D points).

        Returns:
            int: Dimension of the point (always 2 for 2D points).
        """
        return 2


class Vec2:
    """Class representing a 2d vector."""

    def __init__(self, x: Union[int, float], y: Union[int, float]) -> None:
        """
        Initialize the Vec2 object with x and y coordinates.

        args:
        - x (int | float): X-component of the vector.
        - y (int | float): Y-component of the vector.
        """
        self._x = verify_type(x, (int, float))
        self._y = verify_type(y, (int, float))
        self._application_point = Point(0, 0)

    @property
    def x(self) -> Union[int, float]:
        """The x component property value."""
        return self._x

    @x.setter
    def x(self, value: Union[int, float], /) -> None:
        """Set the x component to a given value."""
        verify_type(value, (int, float))
        self._x = value

    @property
    def y(self) -> Union[int, float]:
        """The y component property value."""
        return self._y

    @y.setter
    def y(self, value: Union[int, float], /) -> None:
        """Set the y component to a given value."""
        verify_type(value, (int, float))

        self._y = value

    @property
    def unitary(self) -> "Vec2":
        """
        Gets the unitary vector for an instance.

        Returns:
        - Vec2: The unitary vector.
        """
        return (
            Vec2(self.x / self.modulus, self.y / self.modulus)
            if self.modulus != 0
            else Vec2(0, 0)
        )

    @property
    def modulus(self) -> float:
        """
        Gets the modulus/magnitude of the instance.

        Returns:
        - float: The modulus of the vector.
        """
        return sqrt(self.x**2 + self.y**2)

    @property
    def direction(self) -> float:
        """
        Gets the direction of the vector

        Returns:
        - float: The direction angle in degrees.
        """
        return degrees(atan2(self.y, self.x))

    @property
    def application_point(self) -> Point:
        """
        Gets the application_point value.

        Returns:
        - Point: The application point.
        """
        return self._application_point

    @application_point.setter
    def application_point(
        self,
        value: Union[
            Point, Tuple[Union[int, float], Union[int, float]], List[Union[int, float]]
        ],
    ) -> None:
        """
        Sets the application point of the vector.

        args:
        - value (Point/tuple/list): The value to set as the application point.
        """
        verify_type(value, (Point, tuple, list))
        verify_length(value, 2)

        if isinstance(value, (tuple, list)):
            value = Point(*value)

        self._application_point = value

    @property
    def term_point(self) -> Point:
        """
        Gets the terminal point of the vector.

        Returns:
        - Point: The terminal point of the vector.
        """
        return Point(
            self.x + self.application_point.x, self.y + self.application_point.y
        )

    @property
    def perpendicular(self) -> "Vec2":
        """Gets the perpendicular property."""
        # The dot product with the instance is equal to 0.
        return Vec2(-self.y, self.x)

    def __eq__(self, other: object, /) -> bool:
        """
        Compare if two Vec2 objects are equal.

        Args:
            other (object): The object to compare.

        Returns:
            bool: True if equal, False otherwise.
        """
        if isinstance(other, Vec2):
            return self.x == other.x and self.y == other.y
        return False

    def __ne__(self, other: object, /) -> bool:
        """
        Compare if two Vec2 objects are not equal.

        Args:
            other (object): The object to compare.

        Returns:
            bool: True if not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __getitem__(self, index: int, /) -> Union[int, float]:
        """
        Get the component of Vec2 by index.

        Args:
            index (int): Index of the component (0 for x, 1 for y).

        Returns:
            float: The value of the component.

        Raises:
            IndexError: If index is out of range (not 0 or 1).
        """

        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError(f"Index out of range: {index}")

    def __setitem__(self, index: int, value: Union[int, float], /) -> None:
        """
        Set the component of Vec2 by index.

        Args:
            index (int): Index of the component (0 for x, 1 for y).
            value (int | float): Value to set for the component.

        Raises:
            IndexError: If index is out of range (not 0 or 1).
            TypeError: If value is not numeric (int or float).
        """
        verify_type(index, int)
        verify_type(value, (int, float))

        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value

    def __len__(self) -> int:
        """
        Get the number of components in Vec2.

        Returns:
            int: Always returns 2 for a 2D vector.
        """
        return 2

    def __add__(
        self,
        other: Union[
            "Vec2", Tuple[Union[int, float], Union[int, float]], List[Union[int, float]]
        ],
        /,
    ) -> "Vec2":
        """
        Add another Vec2 or a tuple/list representing a vector.

        Args:
            other (Union["Vec2", tuple[float | int, float | int], list[float | int]]):
                The vector or tuple/list to add.

        Returns:
            Vec2: The resulting Vec2 after addition.

        Raises:
            TypeError: If the operand is not a Vec2, tuple, or list.
        """
        verify_type(other, (Vec2, tuple, list))
        verify_length(other, 2)

        if not isinstance(other, Vec2):
            other = Vec2(*other)

        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(
        self,
        other: Union[
            "Vec2", Tuple[Union[int, float], Union[int, float]], List[Union[int, float]]
        ],
        /,
    ) -> "Vec2":
        """
        Subtract another Vec2 or a tuple/list representing a vector.

        Args:
            other (Union["Vec2", tuple[float, float], list]):
                The vector or tuple/list to subtract.

        Returns:
            Vec2: The resulting Vec2 after subtraction.

        Raises:
            TypeError: If the operand is not a Vec2, tuple, or list.
        """
        verify_type(other, (Vec2, tuple, list))
        verify_length(other, 2)

        if not isinstance(other, Vec2):
            other = Vec2(*other)

        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(
        self,
        other: Union[
            int,
            float,
            "Vec2",
            Tuple[Union[int, float], Union[int, float]],
            List[Union[int, float]],
        ],
        /,
    ) -> Union["Vec2", int | float]:
        """
        Multiply by a scalar or dot product with another Vec2 or vector.

        Args:
            other (Union[int, float, "Vec2", list, tuple]):
                The scalar or vector to multiply with.

        Returns:
            Union[Vec2, float]: The resulting Vec2 after multiplication,
                or a float in case of dot product.

        Raises:
            TypeError: If the operand is not int, float, Vec2, tuple, or list.
            IndexError: If the vector operand does not have 2 dimensions.
        """
        verify_type(other, (int, float, Vec2, list, tuple))

        if isinstance(other, (int, float)):
            return Vec2(self.x * other, self.y * other)

        verify_length(other, 2)

        if not isinstance(other, Vec2):
            other = Vec2(*other)

        return self.dot(other)

    def __rmul__(
        self,
        other: Union[
            int,
            float,
            "Vec2",
            Tuple[Union[int, float], Union[int, float]],
            List[Union[int, float]],
        ],
        /,
    ) -> Union["Vec2", int | float]:
        """
        Multiply the Vec2 by a scalar from the right.

        Args:
            other (Union[int, float]): The scalar to multiply with.

        Returns:
            Vec2: The resulting Vec2 after multiplication.

        Raises:
            TypeError: If the scalar operand is not int or float.
        """
        return self.__mul__(other)

    def __truediv__(self, other: Union[int, float], /) -> "Vec2":
        """
        Divide the Vec2 by a scalar.

        Args:
            other (float): The divisor scalar.

        Returns:
            Vec2: The resulting Vec2 after division.

        Raises:
            TypeError: If the divisor is not int or float.
            ZeroDivisionError: If the divisor is zero.
        """
        verify_type(other, (int, float))

        if other == 0:
            raise ZeroDivisionError("Division by zero is not allowed")

        return Vec2(self.x / other, self.y / other)

    def __neg__(self) -> "Vec2":
        """
        Negate the Vec2 (invert direction).

        Returns:
            Vec2: The negated Vec2.
        """
        return Vec2(-self.x, -self.y)

    def __abs__(self) -> float:
        """
        Get the absolute value (magnitude) of the Vec2.

        Returns:
            float: The magnitude of the Vec2.
        """
        return self.modulus

    def __str__(self) -> str:
        """
        Return a string representation of the Vec2.

        Returns:
            str: The string representation of the Vec2.
        """
        return f"({self.x:.2f}, {self.y:.2f})"

    def __repr__(self) -> str:
        """
        Return a detailed string representation of the Vec2.

        Returns:
            str: The detailed string representation of the Vec2.
        """
        return f"Vec2({self.x:.2f}, {self.y:.2f})"

    @classmethod
    def _from_angle(cls, angle: Union[int, float], /) -> "Vec2":
        """
        Builds the class from a given angle.

        Args:
            angle (Union[int, float]): The given angle.

        Returns:
            Vec2: The instance of the class.
        """
        verify_type(angle, (int, float))

        match angle:
            case 0:
                return cls(1, 0)
            case 90:
                return cls(0, 1)
            case 180:
                return cls(-1, 0)
            case 270:
                return cls(0, -1)
            case _:
                return cls(1, tan(radians(angle)))

    @classmethod
    def _from_points(
        cls,
        a: Union[
            Point, Tuple[Union[int, float], Union[int, float]], List[Union[int, float]]
        ],
        b: Union[
            Point, Tuple[Union[int, float], Union[int, float]], List[Union[int, float]]
        ],
    ):
        """
        Create a Vec2 from two given points.

        Args:
            a (Union[Point, tuple[int | float, int | float], list[int | float]]):
                The starting point of the vector.
            b (Union[Point, tuple[int | float, int | float], list[int | float]]):
                The ending point of the vector.

        Returns:
            Vec2: The Vec2 representing the vector from point a to point b.

        Raises:
            TypeError: If a or b is not a Point, tuple, or list.
            IndexError: If a or b does not have exactly 2 elements.
        """
        verify_type(a, (Point, tuple, list))
        verify_type(b, (Point, tuple, list))

        verify_length(a, 2)
        verify_length(b, 2)

        if not isinstance(a, Point):
            a = Point(*a)

        if not isinstance(b, Point):
            b = Point(*b)

        return cls(b.x - a.x, b.y - a.y)

    @staticmethod
    def calc_modulus(v: Sequence[Union[int, float]]) -> float:
        """
        Calculate the modulus of a 2D vector.

        Args:
            v (Sized): The tuple representing the 2D vector.

        Returns:
            float: The modulus of the vector.
        """
        verify_length(v, 2)
        verify_indexable(v)

        return sqrt(v[0] ** 2 + v[1] ** 2)

    def dot(
        self,
        other: Union[
            "Vec2", Tuple[Union[int, float], Union[int, float]], List[Union[int, float]]
        ],
    ) -> Union[int, float]:
        """
        Calculate the dot product of this vector with another vector.

        Args:
            other (Union["Vec2", list, tuple]): The other vector.

        Returns:
            float: The dot product of the two vectors.

        Raises:
            TypeError: If other is not a Vec2, list, or tuple.
        """
        verify_type(other, (Vec2, tuple, list))
        verify_length(other, 2)

        if not isinstance(other, Vec2):
            other = Vec2(*other)

        return self.x * other.x + self.y * other.y

    def angle(
        self,
        other: Union[
            "Vec2", Tuple[Union[int, float], Union[int, float]], List[Union[int, float]]
        ],
    ) -> float:
        """
        Calculate the angle formed with another vector.

        Args:
            other (Union["Vec2", list, tuple]): The other vector.

        Returns:
            float: The angle between the two vectors in degrees.

        Raises:
            TypeError: If other is not a Vec2, list, or tuple.
        """
        verify_type(other, (Vec2, tuple, list))
        verify_length(other, 2)

        if not isinstance(other, Vec2):
            other = Vec2(*other)

        dot_product = self.dot(other)
        modulus_product = self.modulus * other.modulus

        # Ensure the value is within the valid range for acos to avoid ValueError due to floating-point arithmetic issues.
        cosine_angle = min(1, max(-1, dot_product / modulus_product))
        r = degrees(acos(cosine_angle))
        return round(r, 5) if r < 180 else round(r - 180, 5)


class Line:
    """Class representing a line defined by a vector and a point."""

    def __init__(
        self,
        vector: Union[
            Vec2, Tuple[Union[int, float], Union[int, float]], List[Union[int, float]]
        ],
        point: Union[
            Point, Tuple[Union[int, float], Union[int, float]], List[Union[int, float]]
        ],
        /,
    ) -> None:
        self._vector: Vec2 = (
            Vec2(*verify_length(vector, 2)) if not isinstance(vector, Vec2) else vector
        )
        self._point: Point = (
            Point(*verify_length(point, 2)) if not isinstance(point, Point) else point
        )

    @property
    def vector(self) -> Vec2:
        """Get the vector value."""
        return self._vector

    @vector.setter
    def vector(
        self,
        value: Union[
            Vec2, Tuple[Union[int, float], Union[int, float]], List[Union[int, float]]
        ],
    ) -> None:
        """Modify the vector attribute."""
        verify_type(value, (Vec2, tuple, list))
        verify_length(value, 2)

        if not isinstance(value, Vec2):
            value = Vec2(*value)

        self._vector = value

    @property
    def point(self) -> Point:
        """Get the point value."""
        return self._point

    @point.setter
    def point(
        self,
        value: Union[
            Point, Tuple[Union[int, float], Union[int, float]], List[Union[int, float]]
        ],
    ):
        """Modify the point attribute."""
        verify_type(value, (Point, tuple, list))
        verify_length(value, 2)

        if not isinstance(value, Point):
            value = Point(*value)

        self._point = value

    @property
    def m(self) -> float:
        return self.vector.y / self.vector.x if self.vector.x != 0 else float("inf")

    @property
    def n(self) -> float:
        return (
            self.point.y - self.m * self.point.x
            if self.m != float("inf")
            else self.point.x
        )

    @property
    def orientation(self) -> str:
        _orientation = ""

        if self.m == 0:
            _orientation = "horizontal"

        elif self.m == float("inf"):
            _orientation = "vertical"

        else:
            _orientation = "oblique"

        return _orientation

    @property
    def x_angle(self) -> Union[int, float]:
        return degrees(atan(self.m)) if self.m != float("inf") else 90

    @classmethod
    def _from_points(
        cls,
        a: Union[
            Point, Tuple[Union[int, float], Union[int, float]], List[Union[int, float]]
        ],
        b: Union[
            Point, Tuple[Union[int, float], Union[int, float]], List[Union[int, float]]
        ],
        /,
    ):
        verify_type(a, (Point, tuple, list))
        verify_type(b, (Point, tuple, list))

        verify_length(a, 2)
        verify_length(b, 2)

        if not isinstance(a, Point):
            a = Point(*a)

        if not isinstance(b, Point):
            b = Point(*b)

        return cls(Vec2(b.x - a.x, b.y - a.y), a)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Line):
            return self.vector == other.vector and self.point == other.point
        return False

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __repr__(self) -> str:
        return f"Line(vector = ({self.vector.x}, {self.vector.y}), point({self.point.x}, {self.point.y}))"

    def __str__(self) -> str:
        if self.m == float("inf"):
            return f"x = {self.point.x:.2f}"
        return f"y = {self.m:.2f}x {'+' if self.n >= 0 else '-'} {abs(self.n):.2f}"

    def calc_point(self, x: Union[int, float], /) -> Union[int, float]:
        """
        Returns an existing point for the Line.

        Args:
            x (int/float): The x coordinate.

        Returns:
            (int/float): The calculated point y(x).
        """
        if self.m == float("inf"):
            raise ValueError(
                "Vertical line does not intersect at a specific y for a given x"
            )

        return self.m * x + self.n

    def calc_points(
        self,
        start: Union[int, float],
        end: Union[int, float],
        multiplier: Union[int, float] = 100,
    ) -> list:
        """
        Returns existing points for the Line given [start, end) range for x.

        Args:
            start (int/float): The starting x coordinate.
            end (int/float): The end of range coordinate.
            multiplier (int/float): A multiplier for the amount of points.

        Returns:
            list: A list of the calculated points.
        """
        verify_type(start, (int, float))
        verify_type(end, (int, float))
        verify_type(multiplier, (int, float))

        if end < start:
            start, end = end, start

        if start == end:
            return [self.calc_point(start)]

        # For every unit, (amount) points must be calculated
        return [
            self.calc_point(x / multiplier)
            for x in range(int(start * multiplier), int(end * multiplier))
        ]


class Body:
    """A class representing a physical body with mass, position, speed, size, and color."""

    def __init__(
        self,
        mass: Union[int, float],
        position: Point,
        speed: Vec2,
        size: Tuple[Union[int, float], Union[int, float]],
        color: Tuple[Union[int, float], Union[int, float], Union[int, float]] = (
            0,
            0,
            0,
        ),
    ) -> None:
        """
        Initialize a Body object with mass, position, speed, size, and color.

        Args:
            mass (Union[int, float]): The mass of the body.
            position (Point): The position of the body in 2D space.
            speed (Vec2): The speed (velocity) of the body in 2D space.
            size (Tuple[Union[int, float], Union[int, float]]): The size of the body.
            color (Tuple[Union[int, float], Union[int, float], Union[int, float]], optional):
                The color of the body in RGB format. Defaults to (0, 0, 0).

        Raises:
            TypeError: If any of the input parameters are of incorrect type.
        """
        self._mass: Union[int, float] = verify_type(mass, (int, float))
        self._position: Point = verify_type(position, Point)
        self._x_y_speed: Vec2 = verify_type(speed, Vec2)
        self._size: List[Union[int, float]] = list(
            verify_length(verify_type(size, tuple), 2)
        )
        self._color: Tuple[
            Union[int, float], Union[int, float], Union[int, float]
        ] = verify_length(verify_type(color, tuple), 3)

    @property
    def mass(self) -> Union[int, float]:
        """
        Get the mass of the body.

        Returns:
            Union[int, float]: The mass of the body.
        """
        return self._mass

    @mass.setter
    def mass(self, value: Union[int, float]) -> None:
        """
        Set the mass of the body.

        Args:
            value (Union[int, float]): The new mass value.

        Raises:
            TypeError: If the input value is not an int or float.
        """
        verify_type(value, (int, float))
        self._mass = value

    @property
    def position(self) -> Point:
        """
        Get the position of the body.

        Returns:
            Point: The position of the body.
        """
        return self._position

    @position.setter
    def position(self, value: Point) -> None:
        """
        Set the position of the body.

        Args:
            value (Point): The new position value.

        Raises:
            TypeError: If the input value is not a Point object.
        """
        verify_type(value, Point)
        self._position = value

    @property
    def speed(self) -> Vec2:
        """
        Get the speed (velocity) of the body.

        Returns:
            Vec2: The speed (velocity) of the body.
        """
        return self._x_y_speed

    @speed.setter
    def speed(self, value: Vec2) -> None:
        """
        Set the speed (velocity) of the body.

        Args:
            value (Vec2): The new speed (velocity) value.

        Raises:
            TypeError: If the input value is not a Vec2 object.
        """
        verify_type(value, Vec2)
        self._x_y_speed = value

    @property
    def size(self) -> List[Union[int, float]]:
        """
        Get the size of the body.

        Returns:
            List[Union[int, float]]: The size of the body as [width, height].
        """
        return self._size

    @property
    def size_x(self) -> Union[int, float]:
        """
        Get the width (size along x-axis) of the body.

        Returns:
            Union[int, float]: The width (size along x-axis) of the body.
        """
        return self._size[0]

    @size_x.setter
    def size_x(self, value: Union[int, float]) -> None:
        """
        Set the width (size along x-axis) of the body.

        Args:
            value (Union[int, float]): The new width value.

        Raises:
            TypeError: If the input value is not an int or float.
        """
        verify_type(value, (int, float))
        self._size[0] = value

    @property
    def size_y(self) -> Union[int, float]:
        """
        Get the height (size along y-axis) of the body.

        Returns:
            Union[int, float]: The height (size along y-axis) of the body.
        """
        return self._size[1]

    @size_y.setter
    def size_y(self, value: Union[int, float]) -> None:
        """
        Set the height (size along y-axis) of the body.

        Args:
            value (Union[int, float]): The new height value.

        Raises:
            TypeError: If the input value is not an int or float.
        """
        verify_type(value, (int, float))
        self._size[1] = value

    @property
    def color(self) -> Tuple[Union[int, float], Union[int, float], Union[int, float]]:
        """
        Get the color of the body.

        Returns:
            Tuple[Union[int, float], Union[int, float], Union[int, float]]:
                The color of the body in RGB format.
        """
        return self._color

    @color.setter
    def color(
        self, value: Tuple[Union[int, float], Union[int, float], Union[int, float]]
    ) -> None:
        """
        Set the color of the body.

        Args:
            value (Tuple[Union[int, float], Union[int, float], Union[int, float]]):
                The new color value in RGB format.

        Raises:
            TypeError: If the input value is not a tuple of length 3.
        """
        verify_type(value, tuple)
        verify_length(value, 3)
        self._color = value

    @property
    def x_momentum(self):
        """Gets the momentum property."""
        return self.speed.x * self.mass


class Complex:
    """Class representing a complex number (a + bi)"""

    def __init__(self, re: Union[int, float], imag: Union[int, float]) -> None:
        """
        Initializes a complex number with real part 're' and imaginary part 'imag'.

        Args:
            re (Union[int, float]): Real part of the complex number.
            imag (Union[int, float]): Imaginary part of the complex number.
        """
        self._re = verify_type(re, (int, float))
        self._img = verify_type(imag, (int, float))

    @property
    def real(self) -> Union[int, float]:
        """Gets the real part of the complex number."""
        return self._re

    @real.setter
    def real(self, value: Union[int, float]) -> None:
        """
        Sets the real part of the complex number.

        Args:
            value (Union[int, float]): New value for the real part.
        """
        verify_type(value, (int, float))
        self._re = value

    @property
    def imag(self) -> Union[int, float]:
        """Gets the imaginary part of the complex number."""
        return self._img

    @imag.setter
    def imag(self, value: Union[int, float]) -> None:
        """
        Sets the imaginary part of the complex number.

        Args:
            value (Union[int, float]): New value for the imaginary part.
        """
        verify_type(value, (int, float))
        self._img = value

    @property
    def _b_sing(self):
        """Gets the _b_sing property."""
        return "+" if self._img >= 0 else ""

    @property
    def modulus(self) -> Union[int, float]:
        """Returns the modulus (magnitude) of the complex number."""
        return sqrt(self.real**2 + self.imag**2)

    @property
    def angle(self) -> Union[int, float]:
        """
        Returns the angle (in degrees) of the complex number in the complex plane.

        Returns:
            Union[int, float]: Angle in degrees.
        """
        r_angle = atan(self.imag / self.real)  # Angle in radians.
        return (
            degrees(r_angle)
            if r_angle > 0
            else Complex.simplify_angle(degrees(r_angle))
        )

    @property
    def quadrant(self) -> int:
        """
        Returns the quadrant (1-4) where the complex number lies in the complex plane.

        Returns:
            int: Quadrant number (1, 2, 3, or 4).
        """
        angle = Complex.simplify_angle(self.angle)

        if angle == 0:
            return 0
        elif angle < 90:
            return 1
        elif angle < 180:
            return 2
        elif angle < 270:
            return 3
        else:
            return 4

    @property
    def conjugated(self) -> "Complex":
        """Gets the conjugate property."""
        return Complex(self.real, -self.imag)

    @property
    def opposite(self):
        """Gets the opposite property."""
        return Complex(-self.real, -self.imag)

    def __repr__(self) -> str:
        """
        Returns a string representation of the complex number for debugging.

        Returns:
            str: String representation of the complex number.
        """
        return f"Complex({self.real}{self._b_sing}{self.imag}i)"

    def __str__(self) -> str:
        """
        Returns a string representation of the complex number suitable for display.

        Returns:
            str: String representation of the complex number.
        """
        return f"({self.real}{self._b_sing}{self.imag}i)"

    def __abs__(self) -> Union[int, float]:
        """
        Returns the modulus (magnitude) of the complex number.

        Returns:
            Union[int, float]: Magnitude of the complex number.
        """
        return sqrt(self.real**2 + self.imag**2)

    def __eq__(self, other: object, /) -> bool:
        """
        Checks if two complex numbers are equal.

        Args:
            other (object): Another object to compare with.

        Returns:
            bool: True if equal, False otherwise.
        """
        try:
            verify_type(other, Complex)
        except:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: object, /) -> bool:
        """
        Checks if two complex numbers are not equal.

        Args:
            other (object): Another object to compare with.

        Returns:
            bool: True if not equal, False otherwise.
        """
        return not self.__ne__(other)

    def __neg__(self) -> "Complex":
        """
        Negates the complex number (flips its sign).

        Returns:
            Complex: Negated complex number.
        """
        return self.__mul__(-1)

    def __getitem__(self, index: int) -> Union[int, float]:
        """
        Retrieves the real or imaginary part of the complex number by index.

        Args:
            index (int): Index to specify which part to retrieve (0 for real, 1 for imaginary).

        Returns:
            Union[int, float]: Real or imaginary part of the complex number.
        """
        verify_type(index, int)

        if 0 > index > 1:
            raise IndexError("Index out of range.")

        if index == 0:
            return self.real

        return self.imag

    def __setitem__(self, index: int, value: Union[int, float]) -> None:
        """
        Sets the real or imaginary part of the complex number by index.

        Args:
            index (int): Index to specify which part to set (0 for real, 1 for imaginary).
            value (Union[int, float]): New value for the specified part.

        Raises:
            IndexError: If index is out of range (not 0 or 1).
        """
        verify_type(index, int)
        verify_type(value, (int, float))

        if 0 > index > 1:
            raise IndexError("Index out of range.")

        if index == 0:
            self.real = value
        else:
            self.imag = value

    def __len__(self) -> int:
        """
        Returns the number of components in the complex number (always 2).

        Returns:
            int: Number of components (always 2 for real and imaginary parts).
        """
        return 2

    def __mul__(self, other: Union[int, float, "Complex"]) -> "Complex":
        """
        Multiplies the complex number by another complex number, scalar, or float.

        Args:
            other (Union[int, float, Complex]): Another complex number, scalar, or float.

        Returns:
            Complex: Result of the multiplication.
        """
        verify_type(other, (int, float, Complex))

        if isinstance(other, (int, float)):
            return Complex(self.real * other, self.imag * other)

        return Complex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + other.real * self.imag,
        )

    def __rmul__(self, other: Union[int, float, "Complex"]) -> "Complex":
        """
        Right multiplication of the complex number by another complex number, scalar, or float.

        Args:
            other (Union[int, float, Complex]): Another complex number, scalar, or float.

        Returns:
            Complex: Result of the multiplication.
        """
        return self.__mul__(other)

    def __truediv__(self, other: Union[int, float, "Complex"]) -> "Complex":
        """
        Divides the complex number by another complex number, scalar, or float.

        Args:
            other (Union[int, float, Complex]): Another complex number, scalar, or float.

        Returns:
            Complex: Result of the division.
        """
        verify_type(other, (int, float, Complex))

        if isinstance(other, (int, float)):
            return Complex(self.real / other, self.imag / other)

        return Complex._from_polar(
            self.modulus / other.modulus, self.angle - other.angle
        )

    def __add__(self, other: Union[int, float, "Complex"], /) -> "Complex":
        """
        Adds the complex number to another complex number, scalar, or float.

        Args:
            other (Union[int, float, Complex]): Another complex number, scalar, or float.

        Returns:
            Complex: Result of the addition.
        """
        verify_type(other, (int, float, Complex))

        if isinstance(other, (int, float)):
            return Complex(self.real + other, self.imag)

        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other: Union[int, float, "Complex"], /) -> "Complex":
        """
        Subtracts another complex number, scalar, or float from the complex number.

        Args:
            other (Union[int, float, Complex]): Another complex number, scalar, or float.

        Returns:
            Complex: Result of the subtraction.
        """
        verify_type(other, (int, float, Complex))

        if isinstance(other, (int, float)):
            return Complex(self.real - other, self.imag)

        return Complex(self.real - other.real, self.imag - other.imag)

    def __pow__(
        self, other: Union[int, float, "Complex"]
    ) -> Union["Complex", List["Complex"], int]:
        """
        Raises the complex number to the power of another complex number, scalar, or float.

        Args:
            other (Union[int, float, Complex]): Another complex number, scalar, or float.

        Returns:
            Complex: Result of the exponentiation.
        """
        verify_type(other, (int, float, Complex))

        if isinstance(other, (int, float)):
            return Complex._from_polar(self.modulus**other, self.angle * other)

        raise NotImplemented
        # Exponentiation with another Complex number
        modulus = exp(other.modulus * log(self.modulus) - other.angle * self.angle)
        angle = other.angle * log(self.modulus) + other.modulus * self.angle
        return Complex(modulus, angle)

        return (other * Complex(log(self.modulus), self.angle)) ** e

    @classmethod
    def _from_polar(cls, r: Union[int, float], angle: Union[int, float], /):
        """
        Constructs a complex number from polar coordinates (modulus and angle).

        Args:
            r (Union[int, float]): Modulus (magnitude) of the complex number.
            angle (Union[int, float]): Angle (in degrees) of the complex number.

        Returns:
            Complex: Complex number constructed from polar coordinates.
        """
        verify_type(r, (int, float))
        verify_type(angle, (int, float))

        if angle < 0:
            angle = Complex.simplify_angle(angle)

        return cls(r * degrees(cos(angle)), r * degrees(sin(angle)))

    @staticmethod
    def simplify_angle(angle: Union[int, float]) -> Union[int, float]:
        """
        Normalizes an angle to a standard range [0, 360).

        Args:
            angle (Union[int, float]): Angle to be normalized.

        Returns:
            Union[int, float]: Normalized angle within the range [0, 360).
        """
        verify_type(angle, (int, float))

        if angle == 0:
            return 0
        if angle > 0:
            raise ValueError("Angle already greater than 0.")

        return angle + 360 * int(abs(angle) / 360 + 1)

    # def __plot(self)

    def graph(self) -> None:
        """
        Graphs the complex number in the complex plane.

        """
        plt.figure(figsize=(6, 6))
        plt.quiver(
            0,
            0,
            self.real,
            self.imag,
            angles="xy",
            scale_units="xy",
            scale=1,
            color="blue",
        )
        plt.text(
            self.real / 2 + 1,
            self.imag / 2,
            f"{self.__str__()}",
            color="white",
            fontsize=12,
            ha="left",
            va="bottom",
        )
        plt.text(
            self.real,
            self.imag,
            f"{self.modulus:.2f}",
            color="white",
            fontsize=12,
            ha="left",
            va="bottom",
        )

        # Draw arc for angle
        arc = patches.Arc(
            (0, 0), 2, 2, angle=0, theta1=0, theta2=self.angle, color="red"
        )
        plt.text(
            2.5,
            0,
            f"{self.angle:.2f}°",
            color="red",
            fontsize=12,
            ha="center",
            va="bottom",
        )
        plt.gca().add_patch(arc)
        plt.xlabel("Real Part")
        plt.ylabel("Imaginary Part")
        plt.title("Graph of Complex Number")
        plt.grid(True)
        plt.gca().set_facecolor("black")  # Set background color to black
        plt.xlim(-10, 10)  # Adjust limits for better visualization
        plt.ylim(-10, 10)
        plt.axhline(
            0, color="grey", linewidth=0.5
        )  # Add horizontal and vertical lines for reference
        plt.axvline(0, color="grey", linewidth=0.5)
        plt.show()
