
def readfile(path, *args, **kwargs):
    """
    Reads the file in given path and creates list of points to construct a shape.
    The function assumes that each line is space separated pairs of x y coordinates to draw the shape
    Args:
        path (str): path to a text file to read
        *args:  Variable length arguments list
            **kwargs: Arbitrary keyword arguments
    Returns:
        list: returns list of lists. Each list include pairs of min/max x, y coordinates to construct the shape

    """
    points_list = []
    with open(path) as file:
        file.readline()
        for line in file:
            input_list = line.split()
            points = list(map(float, input_list))
            points_list.append(points)
    return points_list

