"""
Oxygen = 32
Helium = 0
pressure = 200
helium_fill = (pressure*Helium)/100
ozxygen_fill = (((Oxygen*pressure))-(0.21*pressure)+(0.21*helium_fill))/0.79

Air_fill = pressure - helium_fill - ozxygen_fill

print(ozxygen_fill)

"""

"""
ppO2 = 1.4
depth = 50
ideal_nitrox_blend = (ppO2/((depth/10)+1))*100
trimix_end = 40
N2 = (((((trimix_end/10)+1)*0.79))/((depth/10)+1))*100
ideal_trimix = 100-ideal_nitrox_blend-N2
nitrox_end = (((((100-ideal_nitrox_blend)/100)*((depth/10)+1))/0.79)-1)*10
trimix_end_no_input = (((((N2)/100)*((depth/10)+1))/0.79)-1)*10

min_depth = ((0.18/(Oxygen/100))-1)*10
max_depth = ((1.4/(Oxygen/100))-1)*10
"""
"""
Volume = (3.15*8.314*(21+273.15))/(ozxygen_fill*100000)
print(Volume)

"""

Desired_pressure = 200
Desired_o2_mix = .32
Desired_he_mix = 0.0

Start_pressure_mix = 0.0
Start_o2_mix = .21
Start_he_mix = 0.0

Mix_o2_air = 0.21
Mix_n2_air = 1 - Mix_o2_air

Pressure_mix_no_he = Desired_pressure-(Desired_pressure*Desired_he_mix)
Pressure_o2 = Desired_pressure * Desired_o2_mix
Mix_o2_no_he = Pressure_o2/Pressure_mix_no_he

Start_pressure_o2 = Start_pressure_mix * Start_o2_mix
Start_pressure_mix_no_he = Start_pressure_mix-(Start_pressure_mix*Start_he_mix)

if Start_pressure_mix_no_he > 0:
    Start_F_o2_noh = Start_pressure_o2/Start_pressure_mix_no_he
else:
    Start_F_o2_noh = 0

he_fill = Desired_pressure*Desired_he_mix - Start_pressure_mix*Start_he_mix

if he_fill < 0:
    Starting_pressure = (Desired_pressure*Desired_he_mix)/(Start_he_mix)
    print("Lower starting tank pressure to", Starting_pressure)
    
pressure_o2_fill = (Pressure_mix_no_he*(Mix_o2_no_he - Mix_o2_air) - Start_pressure_mix_no_he * (Start_F_o2_noh - Mix_o2_air))/(Mix_n2_air)

if pressure_o2_fill < 0 and Desired_he_mix == 0:

    Starting_pressure = (Desired_pressure*(Desired_o2_mix - Mix_o2_air))/(Start_o2_mix - Mix_o2_air)
    output = f"Please lower the starting tank to {round(Starting_pressure, 1)} bar"

if pressure_o2_fill < 0:
    new_air_fill = (Desired_pressure-Start_pressure_mix) - he_fill
else:
    new_air_fill = (Desired_pressure-Start_pressure_mix) - he_fill - pressure_o2_fill

h_fill = round(he_fill, 1)
o2_fill = round(pressure_o2_fill, 1)
air_fill = round(new_air_fill, 1)

print(h_fill)
print(o2_fill)
print(air_fill)
