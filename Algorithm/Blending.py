"""
    File containing all relevant functions for blending gases.
"""

### TODO ###
# Add Ideal Depth
# Add functions when you need to lower pressure
# Add ability to add gas on top of another gas
# General testing of the whole algorithm

def Blend(new_oxygen, new_helium, new_pressure, old_oxygen, old_helium, old_pressure):
    desiredOxygen = new_oxygen
    desiredHelium = new_helium
    desiredPressure = new_pressure
    startOxygen = old_oxygen
    startHelium = old_helium
    startPressure = old_pressure

    oxygenAir = 0.21 # How much oxygen is in air.
    nitrogenAir = 1 - oxygenAir # How much nitrogen is in air.

    if desiredHelium >= 1:

        return "Can't fill tank with only helium" # TEMP

    if desiredHelium + desiredOxygen > 1:

        return "Doesn't Work" # TEMP

    oxygenPressure = desiredPressure * desiredOxygen # Desired oxygen pressure in the tank
    pressureNitrox = desiredPressure - desiredPressure * desiredHelium # The percentage of tank that is not helium
    oxygenNitrox = oxygenPressure / pressureNitrox # The percentage of oxygen in PressureNitrox
    
    startOxygenPressure = startPressure * startOxygen # How much pressure of oxygen is already in the tank
    startPressureNitrox = startPressure - startPressure * startHelium # How much pressure in the tank that is not helium

    startOxygenFractionNitrox = 0 # What percentage of tank that is not helium

    if startPressureNitrox > 0: # If the blend is a trimix blend

        startOxygenFractionNitrox = startOxygenPressure / startPressureNitrox

    heliumFill = desiredPressure * desiredHelium - startPressure * startHelium # How much helium should be in the tank

    if desiredHelium == 0:

        heliumFill = 0

    if heliumFill < 0: # If some helium should be removed

        lowerPressure = desiredPressure * desiredHelium / startHelium

        if lowerPressure < 1:

            return "Please Empty Tank"

        else:
            return "Lower total pressure to: ", round(lowerPressure - 0.1, 1), "Then fill with:", Blend(desiredOxygen, desiredHelium, desiredPressure, startOxygen, startHelium, round(lowerPressure - 0.1, 1)) # SOMEWHAT TEMP

    oxygenFill = (pressureNitrox * (oxygenNitrox - oxygenAir) - startPressureNitrox * (startOxygenFractionNitrox - oxygenAir)) / nitrogenAir # How much oxygen should be in the tank

    if oxygenFill < 0 and desiredHelium == 0: # If some oxygen should be removed in a nitrox blend

        if startOxygen == oxygenAir: # If Tank is already filled with some air

            return "Please Empty Tank" # TEMP

        else:

            lowerPressure = desiredPressure * (desiredOxygen - oxygenAir) / (startOxygen - oxygenAir)

            if lowerPressure < 1:

                return "Please Empty Tank"

            else:

                return f"Lower total pressure to: {round(lowerPressure - 0.1, 1)} Then fill with: {Blend(desiredOxygen, desiredHelium, desiredPressure, startOxygen, startHelium, round(lowerPressure - 0.1, 1))}"

    airFill = desiredPressure - startPressure - heliumFill # How much air should be in the tank

    if oxygenFill >= 0: # If any oxygen should be added

        airFill -= oxygenFill

    return f"Please fill with {round(oxygenFill, 1)} Bar Oxygen, {round(heliumFill, 1)} Bar Helium, {round(airFill, 1)} Bar Air"

"""
    Testing the algorithm in its current form using the console or this file itself:

    'print(Blend())' will print out how much oxygen, helium and air that is needed to create an EANx32 blend with total pressure of 200bar.
    'print(Blend(0.18, 0.45, 150))' will print out how much oxygen, helium and air that is needed to create a trimix 18/45 with total pressure of 150bar.
    'print(Blend(0.36, 0.0, 175, 0.16, 0.40, 45))' will print out how much oxygen, helium and air that is needed to create a EANx36 blend with toal pressure of 175 when starting with a trimix 16/40 blend of 45bar.

"""