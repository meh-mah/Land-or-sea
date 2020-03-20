import argparse
from i_o.strategy import Function

from structure import LinkedList
from shapes import Rectangle

"""
The main module to run the application.
It accept following parameters:
"-r", "--reader": type of input (currently only "readfile" is supported as an option and is the default one)
"-a", "--arguments": list of arguments to be passed to reader function (if -r readfile you need to add 
    -a <path to a text file to read coordinates>)
"-op", "--output": output graphical result (currently only "TurtleGraphic" is supported as an option. Default to None)
"-z", "--zoom": An integer to define zoom level of graphical drawing starting from 1 for 100% zoom. Default 25


Example:
    $ python -a <path/to/coordinates/file> -op TurtleGraphic -z 25
"""


def main(reader, reader_args, output_type, zoom_level):
    """
    This is the main function to run the script and finding number of lands
    Args:
        reader (str): Name of the function to read and extract data
        reader_args (list): List of arguments to be passed to reader function
        output_type (str): Name of the function to visualize the output
        zoom_level (int): The cartesian coordinates will be multiplied by zoom_level for better visualization

    """
    # get appropriate function to read cartesian coordinates
    read_func = Function.get(reader)
    # read data
    points_list = read_func(*reader_args)

    # create list of Rectangle objects from given cartesian coordinates
    rectangle_list = []
    for points in points_list:
        rectangle = Rectangle(points)
        rectangle_list.append(rectangle)

    # link each rectangle to its immediate outer neighbour and inner neighbour(s).
    # Also tag each rectangle as a land or sea based on immediate neighbour tag
    ll = LinkedList(rectangle_list)
    result, no_of_lands = ll.bfs()
    # output number of rectangles tagged as land
    message = "Found {} land(s)\nout of {} rectangles".format(no_of_lands, len(rectangle_list))
    print(message)
    # output how rectangles are linked with each other
    print(str(ll))

    # if visual display option is activated draw the result
    if output_type:
        output_func = Function.get(output_type)
        output_func(result, message, zoom_level).draw()


if __name__ == '__main__':
    # add arguments
    parser = argparse.ArgumentParser(description="")
    group = parser.add_argument_group('output options')
    group2 = parser.add_argument_group('input options')
    group2.add_argument("-r", "--reader", dest="reader", action="store", default="readfile",
                        help="Input type to read data from (default 'readfile')")
    group2.add_argument("-a", "--arguments", dest="reader_args", action="store", required=True, nargs='+',
                        help="Arguments to be passed to the reader defined in -r option")
    group.add_argument("-op", "--output", dest="output_type", action="store", type=str, default=None,
                       help="Display the result to user additional to the stdout. "
                            "Currently only 'TurtleGraphic' available (Default None)")
    group.add_argument("-z", "--zoom", dest="zoom_level", default=25, action="store", type=int,
                       help="Zoom level if -op is set to 'TurtleGraphic' (Default 25)")

    # parse arguments
    options = parser.parse_args()
    main(**vars(options))
