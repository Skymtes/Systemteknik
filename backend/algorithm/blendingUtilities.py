"""
    File containing utility functions related to blending, but seperated from main file to reduce confusion.
"""

def IdealBlend(depth, endTrimix = None): # What is the ideal blend at a certain depth?

    partialPressure = 1.4

    idealOxygen = partialPressure / (depth / 10 + 1) * 100 # Ideal oxygen in tank at depth, same for nitrox and trimix
    idealNitrogenNitrox = 100 - idealOxygen # Ideal nitrogen in a nitrox blend

    if endTrimix: # If trimix is involved

        idealNitrogenTrimix = ((endTrimix / 10 + 1) * .79) / (depth / 10 + 1) * 100
        idealHelium = 100 - idealOxygen - idealNitrogenTrimix

        return (round(idealOxygen, 1), round(idealHelium, 1), round(idealNitrogenTrimix, 1))

    return (round(idealOxygen, 1), 0, round(idealNitrogenNitrox, 1))

def MaxDepth(oxygen):

    return round((1.4 / oxygen - 1) * 10, 1)

def MinDepth(oxygen):

    return round((.18 / oxygen - 1) * 10, 1)

def EquivalentAirDepth(depth, oxygenPercentage, heliumPercentage = 0):

    nitrogenPercentage = 1 - oxygenPercentage - heliumPercentage

    return round((depth + 10) * nitrogenPercentage / .79 - 10, 1)

def EquivalentNarcoticDepth(depth, oxygenPercentage, heliumPercentage = 0):

    if heliumPercentage == 0:

        nitrogenPercentage = 1 - oxygenPercentage - heliumPercentage

        return round((nitrogenPercentage * (depth / 10 + 1) / .79 - 1) * 10, 1)

    return round((depth + 10) * (1 - heliumPercentage) - 10, 1)