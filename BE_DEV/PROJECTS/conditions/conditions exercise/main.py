# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

weather = ('rainy' or 'sunny' or 'windy' or 'neutral')
time_of_day = ('day' or 'night')
milking_needed = (True) or (False) # Need milking: True or Do not need milking: False
location_cows = ('pasture' or 'cowshed')
season = ('winter' or 'spring' or 'summer' or 'fall')
slurry_tank_full = (True) or (False) # Full: True or Not Full: False
grass_long = (True) or (False) # Grass long: True or Grass short: False


def farm_action(weather, time_of_day, milking_needed, location_cows, season, slurry_tank_full, grass_long):
    if (location_cows == 'pasture' and time_of_day == 'night') or (location_cows == 'pasture' and weather == 'rainy'):
        return ('take cows to cowshed')
    elif (milking_needed == True) and (location_cows == 'cowshed'):
        return ('milk cows')
    elif (milking_needed == True) and (location_cows == 'pasture'):
        return ('take cows to cowshed\nmilk cows\ntake cows back to pasture')
    elif (slurry_tank_full == True) and (location_cows == 'cowshed') and (weather != 'sunny' or 'windy'):
        return ('fertilize pasture')
    elif (slurry_tank_full == True) and (location_cows == 'pasture') and (weather != 'sunny' or 'windy'):
        return ('take cows to cowshed\nfertilize pasture\ntake cows back to pasture')
    elif (grass_long == True) and (season == 'spring') and (location_cows != 'pasture'):
        return ('mow grass')
    elif (grass_long == True) and (season == 'spring') and (location_cows == 'pasture'):
        return ('take cows to cowshed\nmow grass\ntake cows back to pasture')
    else:
        return ('wait')

if __name__ == '__main__':
    farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)
