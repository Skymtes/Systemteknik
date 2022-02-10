"""
Module for handeling all things scuba tank
"""

class Scubatank:
    """
    An instace of this class represents one scuba tank and its contents.
    """

    def __init__(self, capacity, pressure, gasmix):
        """capacity in metric Liters, Pressure in metric Bar, gasmix represented as (oxygen%, nitrogen%, helium%)"""
        self.capacity = capacity
        self.pressure = pressure
        self.gasmix = gasmix

    