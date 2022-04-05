class PPO2:
    """Standard gas blends, gasmix represented as (oxygen%, helium%)"""
    min_ppO2 = (0.18)
    max_ppO2 = (1.6)

def get_preffered_eanx(target_depth):
    target_pressure = (target_depth/10)+1
    oxygen_percent = PPO2.max_ppO2/target_pressure
    return (oxygen_percent, 0.0)
