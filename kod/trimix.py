# Ideal Mix for input depth calculation
ppO2 = 1.4
depth = 100
ideal_nitrox = (ppO2/((depth/10)+1))*100
trimix_end = 40
N2 = (((((trimix_end/10)+1)*0.79))/((depth/10)+1))*100
ideal_trimix = 100-ideal_nitrox-N2

#---------------------------------------------

# EMPTY TANK!!! (vacuum)
P_mix = 200
F_o2 = 0.1
F_o2_air = 0.21
F_n2_air = 1 - F_o2_air
F_h = 0.5

h_fill = P_mix*F_h
h_fill = round(h_fill, 1)
P_mix_noh = P_mix-(P_mix*F_h)
P_o2 = P_mix * F_o2
F_o2_noh = P_o2/P_mix_noh
o2_fill = (P_mix_noh*(F_o2_noh - F_o2_air))/F_n2_air
o2_fill = round(o2_fill, 1)
air_fill = P_mix - h_fill - o2_fill
air_fill = round(air_fill, 1)

print(h_fill)
print(o2_fill)
print(air_fill)

#---------------------------------------------
