from i_o.printer import *
from i_o.reader import *


class Function():
    """
    This is a simple class to implement strategy pattern.
    Responsible to return appropriate function or class at runtime
    """

    @staticmethod
    def get(func_name):
        return globals()[func_name]