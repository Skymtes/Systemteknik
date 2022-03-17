# Ideal Mix for input depth calculation
ppO2 = 1.4
depth = 100
ideal_nitrox = (ppO2/((depth/10)+1))*100
trimix_end = 40
N2 = (((((trimix_end/10)+1)*0.79))/((depth/10)+1))*100
ideal_trimix = 100-ideal_nitrox-N2

#---------------------------------------------
F_o2_air = 0.21
F_n2_air = 1 - F_o2_air

P_o_mix = 100
F_o_o2 = 0.5
F_o_h = 0.5

P_n_mix = 100
F_n_o2 = 0.75
F_n_h = 0.25

h_empty = 0
h_diff = (F_n_h * P_n_mix)-(F_o_h * P_o_mix)
print(h_diff)
if h_diff < 0:
    h_empty = P_o_mix + h_diff
    print("h lower tank pressure to", P_o_mix + h_diff)



he_fill = P_n_mix*F_n_h
he_fill = round(he_fill, 1)
P_mix_noh = P_n_mix-(P_n_mix*F_n_h)
P_o2 = P_n_mix * F_n_o2
F_o2_noh = P_o2/P_mix_noh
o2_fill = (P_mix_noh*(F_o2_noh - F_o2_air))/F_n2_air
o2_fill = round(o2_fill, 1)
air_fill = P_n_mix - he_fill - o2_fill
air_fill = round(air_fill, 1)

print("h", he_fill)
print("o", o2_fill)
print("a", air_fill)

#---------------------------------------------

# EMPTY TANK!!! (vacuum)
P_mix = 200
F_o2 = 0.1
F_o2_air = 0.21
F_n2_air = 1 - F_o2_air
F_he = 0.5

he_fill = P_mix*F_he
he_fill = round(he_fill, 1)
P_mix_noh = P_mix-(P_mix*F_he)
P_o2 = P_mix * F_o2
F_o2_noh = P_o2/P_mix_noh
o2_fill = (P_mix_noh*(F_o2_noh - F_o2_air))/F_n2_air
o2_fill = round(o2_fill, 1)
air_fill = P_mix - he_fill - o2_fill
air_fill = round(air_fill, 1)

#print(h_fill)
#print(o2_fill)
#print(air_fill)

#---------------------------------------------
