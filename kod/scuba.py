"""
Module for handeling all things scuba
"""

class StandardBlends:
    """Standard gas blends"""
    Air = (0.21, 0.79, 0.0)
    EAN32 = (0.32, 0.68, 0.0)
    EAN36 = (0.36, 0.64, 0.0)

    def EAN(x):
        if isinstance(x, int) or isinstance(x, float):
            x = x/100
            return (x, 1-x, 0.0)
        else:
            raise ValueError



class GasPurity:
    """Standard gas blends"""
    # False presumption that both gases are 100% pure
    oxygen = 1
    helium = 1


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

        # Temporary calculation until algorithm is complete
        print(StandardBlends.Air[0])
        print(GasPurity.oxygen)
        print(self.desiredpressure)
        print(self.desiredgasmix[0])
        print(self.pressure)
        print(self.gasmix[0])

        oxygen_fill_pressure = (self.desiredpressure*(self.desiredgasmix[0] - StandardBlends.Air[0])
                                - self.pressure*(self.gasmix[0] - StandardBlends.Air[0])
                                / (GasPurity.oxygen - StandardBlends.Air[0]))
        print(oxygen_fill_pressure)

        if oxygen_fill_pressure < 0:
            starting_pressure = (self.desiredpressure*(self.desiredgasmix[0] - StandardBlends.Air[0])
                                / (self.gasmix[0] - StandardBlends.Air[0]))
            print(starting_pressure)
        
        return

    def fill_completed(self):
        """Sets new pressure and mix in the tank after successful fill"""
        self.pressure = self.desiredpressure
        self.desiredpressure = None
        self.gasmix = self.desiredgasmix
        self.desiredgasmix = None
