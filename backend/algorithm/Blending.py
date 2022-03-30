"""
    File containing all relevant functions for blending gases.
"""

### TODO ###
# Add Ideal Depth
# Add ability to add gas on top of another gas
# General testing of the whole algorithm


def Blend(desiredOxygen = 0.32, desiredHelium = 0.0, desiredPressure = 200.0, startOxygen = 0.21, startHelium = 0.0, startPressure = 0.0):

    """Function used for blending gases.
    
        desiredOxygen: What percentage of oxygen the tank should have.
        desiredHelium: What percentage of helium the tank should have.
        desiredPressure: How much pressure in the tank is desired.
        startOxygen: What percentage of oxygen the tank is currently filled with.
        startHelium: What percentage of helium the tank is  currently filled with.
        startPressure: How much pressure of gases the tank is filled with.

        returns (oxygen, helium, air) all measured in pressure to fill.
    """

    oxygenAir = 0.21 # How much oxygen is in air.
    nitrogenAir = 1 - oxygenAir # How much nitrogen is in air.

    oxygenPressure = desiredPressure * desiredOxygen # Desired oxygen pressure in the tank
    pressureNitrox = desiredPressure - desiredPressure * desiredHelium # The percentage of tank that is not helium
    oxygenNitrox = oxygenPressure / pressureNitrox # The percentage of oxygen in PressureNitrox
    
    startOxygenPressure = startPressure * startOxygen # How much pressure of oxygen is already in the tank
    startPressureNitrox = startPressure - startPressure * startHelium # How much pressure in the tank that is not helium

    startOxygenFractionNitrox = 0 # What percentage of tank that is not helium

    if startPressureNitrox > 0: # If the blend is a trimix blend

        startOxygenFractionNitrox = startOxygenPressure / startPressureNitrox

    heliumFill = desiredPressure * desiredHelium - startPressure * startHelium # How much helium should be in the tank

    if heliumFill < 0: # If some helium should be removed

        lowerHelium = desiredPressure * desiredHelium / startHelium # How much helium should be left

        if lowerHelium < 1:

            return EmptyTank(startOxygen, startHelium, startPressure) # Empties Tank

        else:
            
            heliumDiff = round(lowerHelium - startHelium * startPressure, 1) # Difference in starting helium from how much helium it should have

            return (0, heliumDiff, 0)

    oxygenFill = (pressureNitrox * (oxygenNitrox - oxygenAir) - startPressureNitrox * (startOxygenFractionNitrox - oxygenAir)) / nitrogenAir # How much oxygen should be in the tank

    if oxygenFill < 0 and desiredHelium == 0: # If some oxygen should be removed in a nitrox blend

        if startOxygen == oxygenAir: # If Tank is already filled with some air

            return EmptyTank(startOxygen, startHelium, startPressure) # Empties Tank

        else:

            lowerOxygen = desiredPressure * (desiredOxygen - oxygenAir) / (startOxygen - oxygenAir) # How much oxygen should be left, pressure

            if lowerOxygen < 1:

                return EmptyTank(startOxygen, startHelium, startPressure) # Empties Tank

            else:
                
                oxygenDiff = round(lowerOxygen - startOxygen * startPressure, 1) # Difference in starting oxygen from how much oxygen it should have, pressure

                return (oxygenDiff, 0, 0)

    airFill = desiredPressure - startPressure - heliumFill # How much air should be in the tank

    if oxygenFill >= 0: # If any oxygen should be added

        airFill -= oxygenFill

    return (round(oxygenFill, 1), round(heliumFill, 1), round(airFill, 1)) # Returns how much oxygen, helium and air should be added, measured in bar

def EmptyTank(startOxygen, startHelium, startPressure): # How much oxygen, helium and air should be emptied for the tank to be empty

    oxygenFraction = startOxygen * startPressure # Percentage of oxygen in tank
    heliumFraction = startHelium * startPressure # Percentage of helium in tank

    return (-oxygenFraction, -heliumFraction, -(startPressure - oxygenFraction - heliumFraction))

"""
    Testing the algorithm in its current form using the console or this file itself:

    'print(Blend())' will print out how much oxygen, helium and air that is needed to create an EANx32 blend with total pressure of 200bar.
    'print(Blend(0.18, 0.45, 150))' will print out how much oxygen, helium and air that is needed to create a trimix 18/45 with total pressure of 150bar.
    'print(Blend(0.36, 0.0, 175, 0.16, 0.40, 45))' will print out how much oxygen, helium and air that is needed to create a EANx36 blend with toal pressure of 175 when starting with a trimix 16/40 blend of 45bar.

"""