#Calculating with an "empty tank"

def calculate_empty():
    Oxygen_air = 0.209
    Nitrogen_air = 1 - Oxygen_air
    Desired_pressure = 204
    Desired_oxygen_mix = 0.32
    Pressure_add_oxygen = (Desired_pressure*(Desired_oxygen_mix - Oxygen_air))/Nitrogen_air
    print(f"Please add {Pressure_add_oxygen} bar of oxygen and then top up to {Desired_pressure} bar")
    return

#Calculate fill gas with tank not empty

def calculate_not_empty():
    Pressure_mix_start = 26
    Start_oxygen_mix = 0.36
    Desired_gas_mix = 0.32
    Desired_pressure = 204
    Oxygen_air = 0.209
    Oxygen_fill = 1.0

    Pressure_oxygen_fill = (Desired_pressure * (Desired_gas_mix - Oxygen_air) - Pressure_mix_start * (Start_oxygen_mix - Oxygen_air))/(Oxygen_fill - Oxygen_air)
    print(f"Please add {Pressure_oxygen_fill} bar of oxygen")
    Pressure_top_up_air = Desired_pressure - Pressure_mix_start - Pressure_oxygen_fill
    print(f"Please top up with {Pressure_top_up_air} bar of air")
    if Pressure_oxygen_fill < 0:
        Starting_pressure = (Desired_pressure*(Desired_gas_mix - Oxygen_air))/(Start_oxygen_mix - Oxygen_air)
        print(f"Please lower the starting tank to {Starting_pressure} bar")
    return



