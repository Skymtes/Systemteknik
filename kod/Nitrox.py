"""
    Used for calculating several Nitrox blends
"""

# Default function which recieves parameters and decides what calculation should be done

def nitrox(Desired_oxygen_mix = 0.32, Desired_pressure = 200, Start_oxygen_mix = 0.21, Start_pressure_mix = None):

    if Start_oxygen_mix == 0.21:

        return calculate_empty(Desired_pressure, Desired_oxygen_mix)

    else:

        return calculate_not_empty(Desired_oxygen_mix, Desired_pressure, Start_pressure_mix, Start_oxygen_mix)

# Calculating with an "empty tank"

def calculate_empty(Desired_pressure, Desired_oxygen_mix):

    Oxygen_air = 0.209
    Nitrogen_air = 1 - Oxygen_air
    # Desired_pressure = 204
    # Desired_oxygen_mix = 0.32

    Pressure_add_oxygen = (Desired_pressure*(Desired_oxygen_mix - Oxygen_air))/Nitrogen_air
    
    return f"Please add {round(Pressure_add_oxygen, 2)} bar of oxygen\nPlease top up to {round(Desired_pressure, 2)} bar"

# Calculate fill gas with tank not empty / partially filled

def calculate_not_empty(Desired_oxygen_mix, Desired_pressure, Pressure_mix_start, Start_oxygen_mix):

    # Pressure_mix_start = 26
    # Start_oxygen_mix = 0.36
    # Desired_oxygen_mix = 0.32
    # Desired_pressure = 204
    Oxygen_air = 0.209
    Oxygen_fill = 1.0

    if Desired_oxygen_mix < Oxygen_air:

        return "Desired oxygen is too low!"

    Pressure_oxygen_fill = (Desired_pressure * (Desired_oxygen_mix - Oxygen_air) - Pressure_mix_start * (Start_oxygen_mix - Oxygen_air))/(Oxygen_fill - Oxygen_air)
    
    if Pressure_oxygen_fill < 0:

        Starting_pressure = (Desired_pressure*(Desired_oxygen_mix - Oxygen_air))/(Start_oxygen_mix - Oxygen_air)
        output = f"Please lower the starting tank to {round(Starting_pressure, 2)} bar"

    else:

        output = f"Please add {round(Pressure_oxygen_fill, 2)} bar of oxygen"

    # Pressure_top_up_air = Desired_pressure - Pressure_mix_start - Pressure_oxygen_fill
    # output += f"\nPlease top up with {round(Pressure_top_up_air, 2)} bar of air"

    output += f"\nPlease top up to {round(Desired_pressure, 2)} bar"

    return output

print(nitrox(0.36, 204, 0.21))
print(nitrox(0.36, 204, 0.21, 1))
# print(nitrox())