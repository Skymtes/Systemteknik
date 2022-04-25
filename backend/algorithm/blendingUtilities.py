"""
    File containing utility functions related to blending, but seperated from main file to reduce confusion.
"""

def IdealBlend(depth, partialPressure = 1.4 , endTrimix = None): # What is the ideal blend at a certain depth?

    idealOxygen = partialPressure / (depth / 10 + 1) * 100 # Ideal oxygen in tank at depth, same for nitrox and trimix
    idealNitrogenNitrox = 100 - idealOxygen # Ideal nitrogen in a nitrox blend

    if endTrimix: # If trimix is involved

        idealNitrogenTrimix = ((endTrimix / 10 + 1) * .79) / (depth / 10 + 1) * 100 # Ideal nitrogen percentage in a trimix mix
        idealHelium = 100 - idealOxygen - idealNitrogenTrimix # Ideal helium percentage in a trimix mix

        return (round(idealOxygen, 1), round(idealHelium, 1), round(idealNitrogenTrimix, 1))

    return (round(idealOxygen, 1), 0, round(idealNitrogenNitrox, 1))

def MaxDepth(oxygen, partialPressure = 1.4): # Returns max operating depth based on percentage of oxygen

    return round((partialPressure / oxygen - 1) * 10, 1)

def MinDepth(oxygen): # Returns minimum operating depth on percentage of oxygen

    return round((.18 / oxygen - 1) * 10, 1)

def EquivalentAirDepth(depth, oxygenPercentage, heliumPercentage = 0): # Returns the equivalent air depth of blend at specific depth

    nitrogenPercentage = 1 - oxygenPercentage - heliumPercentage

    return round((depth + 10) * nitrogenPercentage / .79 - 10, 1)

def EquivalentNarcoticDepth(depth, heliumPercentage): # Returns the equivalent nartcotic depth of trimix blend at specific depth

    return round((depth + 10) * (1 - heliumPercentage) - 10, 1)