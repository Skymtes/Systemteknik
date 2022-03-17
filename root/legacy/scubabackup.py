"""
Module for handeling all things scuba
"""

import save
import datetime

class StandardBlends:
    """Standard gas blends, gasmix represented as (oxygen%, helium%)"""
    Air = (0.21, 0.0)
    EAN32 = (0.32, 0.0)
    EAN36 = (0.36, 0.0)

    def EAN(x):
        if isinstance(x, int) or isinstance(x, float):
            x = x/100
            return (x, 0.0)
        else:
            raise ValueError

    def Tx(o2, he):
        if (isinstance(o2, int) or isinstance(o2, float)) and (isinstance(he, int) or isinstance(he, float)):
            o2 = o2/100
            he = he/100
            return (o2, he)
        else:
            raise ValueError

#CURRENT IMPLEMENTATION CAN NOT USE THIS
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
        """capacity in metric Liters, Pressure in metric Bar, gasmix represented as (oxygen%, helium%)"""
        self.capacity = capacity
        self.pressure = pressure
        self.gasmix = gasmix

        self.gasmix_min_depth, self.gasmix_max_depth = self.depth_min_max()

        self.desired_pressure = None
        self.desired_gasmix = None
        
        self.fill_date = None


    def set_tank_fill(self, desired_pressure, desired_gasmix):
        self.desired_pressure = desired_pressure
        self.desired_gasmix = desired_gasmix

        save.set_tank_fill(desired_pressure, desired_gasmix)


    def trimix(self):

        self.fill_completed()


    def depth_min_max(self):
        min_depth = ((0.16/self.gasmix[0])-1)*10 #HYPOXIA LIMIT
        max_depth = ((1.6/self.gasmix[0])-1)*10 #OXYGEN TOXICITY LIMIT
        return min_depth, max_depth
        

    def fill_completed(self):
        """Sets new pressure and mix in the tank after successful fill"""
        self.fill_date = datetime.datetime.now()
        save.set_tank_fill_date(self.fill_date)

        self.pressure = self.desiredpressure
        self.desiredpressure = None
        self.gasmix = self.desiredgasmix
        self.desiredgasmix = None

