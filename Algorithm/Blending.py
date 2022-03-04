"""
    File containing all relevant functions for blending gases.
"""

### TODO ###
# Add Ideal Depth

def Blend(desiredOxygen = 0.32, desiredHelium = 0.0, desiredPressure = 200.0, startOxygen = 0.21, startHelium = 0.0, startPressure= 0.0):

    """Function used for blending gases.
    
        desiredOxygen: What percentage of oxygen the tank should have.
        desiredHelium: What percentage of helium the tank should have.
        desiredPressure: How much pressure in the tank is desired.
        startOxygen: What percentage of oxygen the tank is currently filled with.
        startHelium: What percentage of helium the tank is  currently filled with.
        startPressure: How much pressure of gases the tank is filled with.

        returns (oxygen, helium, air)
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

        lowerPressure = desiredPressure * desiredHelium / startHelium

    oxygenFill = (pressureNitrox * (oxygenNitrox - oxygenAir) - startPressureNitrox * (startOxygenFractionNitrox - oxygenAir)) / nitrogenAir # How much oxygen should be in the tank

    if oxygenFill < 0 and desiredHelium == 0: # If some oxygen should be removed in a nitrox blend

        lowerPressure = desiredPressure * (desiredOxygen - oxygenAir) / (startOxygen - oxygenAir)

    airFill = desiredPressure - startPressure - heliumFill # How much air should be in the tank

    if oxygenFill >= 0: # If any oxygen should be added

        airFill -= oxygenPressure

    return (round(oxygenFill, 1), round(heliumFill, 1), round(airFill, 1)) # Returns how much oxygen, helium and air should be added, measured in bar
    