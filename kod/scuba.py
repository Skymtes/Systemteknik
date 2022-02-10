"""
Module for handeling all things scuba
"""

class Tank:
    """
    An instace of this class represents one scuba tank and its contents.
    """

    def __init__(self, capacity, pressure, gasmix):
        """capacity in metric Liters, Pressure in metric Bar, gasmix represented as (oxygen%, nitrogen%, helium%)"""
        self.capacity = capacity
        self.pressure = pressure
        self.gasmix = gasmix

        self.desiredpressure = None
        self.desiredgasmix = None

    def set_desired_pressure(self, desired_pressure):
        self.desiredpressure = desired_pressure
        return

    def set_desired_gasmix(self, desired_gasmix):
        self.desiredgasmix = desired_gasmix
        return

    def fill(self):
        """
        1. Calculate if the tube needs to release some of the gas that is currently inside.

        2. Calculate how much of each gas is needed for the correct blend.
        Count gases as air, oxygen and helium and NOT as nitrogen, oxygen and helium.

        3. Calculate the blends max and min depth and check if that is reasonable.

        4. Calculate the total cost of the tube.
        """
        return

class StandardBlends:
    """Standard gas blends"""
    Air = (21, 79, 0)
    EAN32 = (32, 68, 0)
    EAN36 = (36, 64, 0)