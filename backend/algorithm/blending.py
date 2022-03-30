"""
    File containing all relevant functions for blending gases.
"""

### TODO ###
# Add Ideal Depth
# Add functions when you need to lower pressure
# Add ability to add gas on top of another gas
# General testing of the whole algorithm


def Blend(desiredOxygen = None , desiredHelium = None, desiredPressure = None, startOxygen = None, startHelium = None , startPressure = None):
    """
    Function used for blending gases.
    
    desiredOxygen: What percentage of oxygen the tank should have.
    desiredHelium: What percentage of helium the tank should have.
    desiredPressure: How much pressure in the tank is desired.
    startOxygen: What percentage of oxygen the tank is currently filled with.
    startHelium: What percentage of helium the tank is  currently filled with.
    startPressure: How much pressure of gases the tank is filled with.
    returns (oxygen, helium, air) all measured in pressure to fill.
    """
    args = [desiredOxygen , desiredHelium, desiredPressure, startOxygen, startHelium , startPressure]
    for idx,value in enumerate(args):
        if value == None:
            return "Invaild input : missing arg"
        elif type(value) == str:
            return "Invaild input : input as str"

    range_check_1 = 0 <= (desiredOxygen or desiredHelium or startOxygen or startHelium) <= 1
    if range_check_1 is False : return "Invaild input : range limit"
    range_check_300 = 0 <= (desiredPressure or startPressure) <= 300
    if range_check_300 is False : return 
    oxygenAir = 0.21 # How much oxygen is in air.
    nitrogenAir = 1 - oxygenAir # How much nitrogen is in air.
    oxygenPressure = desiredPressure * desiredOxygen # Desired oxygen pressure in the tank
    pressureNitrox = desiredPressure - desiredPressure * desiredHelium # The percentage of tank that is not helium
    try:
        oxygenNitrox = oxygenPressure / pressureNitrox # The percentage of oxygen in PressureNitrox
    except ZeroDivisionError:
        return("Can not by devied by zero")
    
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

                return "Lower total pressure to: ", round(lowerPressure - 0.1, 1), "Then fill with:", Blend(desiredOxygen, desiredHelium, desiredPressure, startOxygen, startHelium, round(lowerPressure - 0.1, 1)) # SOMEWHAT TEMP

    airFill = desiredPressure - startPressure - heliumFill # How much air should be in the tank

    if oxygenFill >= 0: # If any oxygen should be added

        airFill -= oxygenFill

    return (round(oxygenFill, 1), round(heliumFill, 1), round(airFill, 1)) # Returns how much oxygen, helium and air should be added, measured in bar

"""
    Testing the algorithm in its current form using the console or this file itself:
    'print(Blend())' will print out how much oxygen, helium and air that is needed to create an EANx32 blend with total pressure of 200bar.
    'print(Blend(0.18, 0.45, 150))' will print out how much oxygen, helium and air that is needed to create a trimix 18/45 with total pressure of 150bar.
    'print(Blend(0.36, 0.0, 175, 0.16, 0.40, 45))' will print out how much oxygen, helium and air that is needed to create a EANx36 blend with toal pressure of 175 when starting with a trimix 16/40 blend of 45bar.
"""


print(Blend(62,0,40,32,0,180))