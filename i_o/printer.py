import turtle
from abc import ABC, abstractmethod


class Graphic(ABC):
    """
    Abstract class to draw shapes on screen
    """
    # set global color for land and sea (land=green, sea=light blue)
    color_dict = {True: 'green',
                  False: 'light blue'}

    def __init__(self, result, message):
        """

        Args:
            result (dict): A dictionary of 'Node' object(s) as value and associated level in the linkedlist tree as a key
            message (str): Message to be displayed
        Attributes:
            result (dict): A dictionary of 'Node' object(s) as value and associated level in the linkedlist tree as a key
            message (str): Message to be displayed
        """
        self.result = result
        self.message = message

    @abstractmethod
    def draw(self):
        pass


class TurtleGraphic(Graphic):
    """
    Implementation of abstract Graphic class.
    This implementation uses python turtle to draw lands and seas on the screen
    """

    def __init__(self, *args, **kwargs):
        """
        Args:
            *args:  Variable length arguments list to be passed to Graphic class.
                At index 2 includes an integer to zoom the rectangles
            **kwargs: Arbitrary keyword arguments
        Attributes:
            zoom (int): an integer to zoom the shape
            style (tuple): tuple of (font, size, font style)
        """
        Graphic.__init__(self, *args[:2])
        self.zoom = args[2]
        self.style = ('Courier', 15, 'bold')

        # initialize turtle object
        turtle.title("Earth")
        turtle.resizemode("auto")
        turtle.speed("fastest")
        turtle.bgcolor("light blue")

    def draw(self):
        """
        Draws lands and seas on the screen
        """
        # draw rectangles based on information from Node object
        for k, v in self.result.items():
            for node in v:
                # set appropriate color
                color = self.color_dict[k%2]
                turtle.color(color, color)
                # get appropriate function to draw shape based on type of the shape
                getattr(self, "draw_"+type(node.data).__name__.lower())(node.data, self.zoom)

        # write the given text message
        turtle.color('deep pink')
        self.write_msg(self.message, self.style)

        # hide the cursor
        turtle.hideturtle()
        # enter mainloop and wait until user closes the turtle screen
        # turtle.Screen().exitonclick()
        turtle.done()

    @staticmethod
    def write_msg(message, style):
        """
        write the result in text format on the screen
        Args:
            message (str): Message to be displayed
            style (tuple): tuple of (font, size, font style). E.g. ('Courier', 15, 'bold')
        """

        turtle.penup()
        turtle.goto((-1 * turtle.Screen().window_width() / 2) + 10, turtle.Screen().window_height() / 4)
        turtle.pendown()
        turtle.write(message, font=style, align='left')

    @staticmethod
    def draw_rectangle(rectangle, zoom):
        """
        Draw rectangle based on the given coordinates in the Rectangle object
        Args:
            rectangle (Rectangle): A Rectangle object to draw
            zoom (int): an integer to zoom the shape
        """

        # get min point of the rectangle
        min_x = rectangle.min_point.x * zoom
        min_y = rectangle.min_point.y * zoom

        # move the pen to min point
        turtle.penup()
        turtle.goto(min_x, min_y)
        turtle.pendown()

        # start drawing
        turtle.begin_fill()
        turtle.forward(rectangle.width * zoom)
        turtle.left(90)
        turtle.forward(rectangle.height * zoom)
        turtle.left(90)
        turtle.forward(rectangle.width * zoom)
        turtle.left(90)
        turtle.forward(rectangle.height * zoom)
        turtle.left(90)
        turtle.end_fill()