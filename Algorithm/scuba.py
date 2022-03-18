"""
Module for handeling all things scuba
"""

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

    def Tx(o, h):
        if (isinstance(o, int) or isinstance(o, float)) and (isinstance(h, int) or isinstance(h, float)):
            o = o/100
            h = h/100
            return (o, h)
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

    def __init__(self, capacity, pressure, gasmix, desiredpressure, desiredgasmix):
        """capacity in metric Liters, Pressure in metric Bar, gasmix represented as (oxygen%, helium%)"""
        self.capacity = capacity
        self.pressure = pressure
        self.gasmix = gasmix

        self.gasmix_min_depth, self.gasmix_max_depth = self.depth_min_max()

        self.desiredpressure = desiredpressure
        self.desiredgasmix = desiredgasmix

    def Nitrox(self):
        # Temporary NITROX ONLY calculation until algorithm is complete
        oxygen_fill_pressure = (self.desiredpressure*(self.desiredgasmix[0] - StandardBlends.Air[0])
                                - self.pressure*(self.gasmix[0] - StandardBlends.Air[0])
                                / (GasPurity.oxygen - StandardBlends.Air[0]))
        print(oxygen_fill_pressure)

        if oxygen_fill_pressure < 0:
            starting_pressure = (self.desiredpressure*(self.desiredgasmix[0] - StandardBlends.Air[0])
                                / (self.gasmix[0] - StandardBlends.Air[0]))
            print(starting_pressure)
        
        return

    def trimix_empty_tank(self):
        # EMPTY TANK!!! (vacuum)
        h_fill = self.desiredpressure*self.desiredgasmix[1]
        h_fill = round(h_fill, 1)
        P_mix_no_h = self.desiredpressure-(self.desiredpressure*self.desiredgasmix[1])
        P_o2 = self.desiredpressure * self.desiredgasmix[0]
        F_o2_no_h = P_o2/P_mix_no_h
        o2_fill = (P_mix_no_h*(F_o2_no_h - StandardBlends.Air[0]))/(1-StandardBlends.Air[0])
        o2_fill = round(o2_fill, 1)
        air_fill = self.desiredpressure - h_fill - o2_fill
        air_fill = round(air_fill, 1)

        h_l = self.capacity*h_fill
        o2_l = self.capacity*o2_fill
        air_l = self.capacity*air_fill

        self.fill_completed(h_l, o2_l, air_l)
        
        #TEMPORARY DEBUGGING
        print("h in Liter", h_fill*self.capacity)
        print("o2 in liter", o2_fill*self.capacity)
        print("air in liter", air_fill*self.capacity)
        #-------------------

        return h_l, o2_l, air_l


    def depth_min_max(self):
        min_depth = ((0.16/self.gasmix[0])-1)*10 #HYPOXIA LIMIT
        max_depth = ((1.6/self.gasmix[0])-1)*10 #OXYGEN TOXICITY LIMIT
        return min_depth, max_depth
        

    def fill_completed(self, h_l, o2_l, air_l):
        """Sets new pressure and mix in the tank after successful fill"""
        self.pressure = self.desiredpressure
        self.desiredpressure = None
        self.gasmix = self.desiredgasmix
        self.desiredgasmix = None
