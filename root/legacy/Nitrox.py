"""
    Used for calculating several Nitrox blends
"""

# Default function which recieves parameters and decides what calculation should be done

def nitrox(Desired_oxygen_mix = 0.32, Desired_pressure = 200, Start_oxygen_mix = 0.21, Start_pressure_mix = None):

    """Default Nitrox-algorithm which calculates how to create a nitrox-blend depending on desired O2 and desired pressure, as well as starting O2 and starting pressure. Default values gives a EANx32 blend."""

    if Start_oxygen_mix == 0.21:

        return calculate_empty(Desired_oxygen_mix, Desired_pressure)

    else:

        return calculate_not_empty(Desired_oxygen_mix, Desired_pressure, Start_oxygen_mix, Start_pressure_mix)

# Calculating with an "empty tank"

def calculate_empty(Desired_oxygen_mix, Desired_pressure):

    """Function to calculate nitrox-blend when tank is 'empty', i.e. only filled with air, depending on the desired O2 and desired pressure."""

    Oxygen_air = 0.21
    Nitrogen_air = 1 - Oxygen_air

    Pressure_add_oxygen = (Desired_pressure*(Desired_oxygen_mix - Oxygen_air))/Nitrogen_air
    
    return f"Please add {round(Pressure_add_oxygen, 1)} bar of oxygen\nPlease top up to {round(Desired_pressure, 1)} bar"

# Calculate fill gas with tank not empty / partially filled

def calculate_not_empty(Desired_oxygen_mix, Desired_pressure, Start_oxygen_mix, Start_pressure_mix):

    """Function to calculate nitrox-blend when tank is 'not empty', i.e. when another blend is already in the tank, depending on desired O2 and desired pressure, as well as starting O2 and starting pressure."""

    Oxygen_air = 0.21
    Oxygen_fill = 1.0

    if Desired_oxygen_mix < Oxygen_air:

        return "Desired oxygen is too low!"

    Pressure_oxygen_fill = (Desired_pressure * (Desired_oxygen_mix - Oxygen_air) - Start_pressure_mix * (Start_oxygen_mix - Oxygen_air))/(Oxygen_fill - Oxygen_air)
    
    if Pressure_oxygen_fill < 0:

        Starting_pressure = (Desired_pressure*(Desired_oxygen_mix - Oxygen_air))/(Start_oxygen_mix - Oxygen_air)
        output = f"Please lower the starting tank to {round(Starting_pressure, 1)} bar"

    else:

        output = f"Please add {round(Pressure_oxygen_fill, 1)} bar of oxygen"

    output += f"\nPlease top up to {round(Desired_pressure, 1)} bar"

    return output

# print(nitrox(0.36, 200, 0.21, 1))
# print(nitrox(0.36, 200, 0.21, 100))
# print(nitrox())