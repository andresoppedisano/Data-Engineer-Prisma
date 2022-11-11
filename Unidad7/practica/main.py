from tkinter import N
from unittest import result


import logging

def show_docstring():
    """Descripcion de la funcion impresionnnnn"""
    pass

show_docstring.__doc__








def getLevelName(level):

    result=_levelToName.get(level)
    if result is not None:
        return result
    result = _nameToLevel.get(level)
    if result is not None:
        return result
    return "Level %s" % level
