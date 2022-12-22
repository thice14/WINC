# PART 1
#1.
gullit = 'Ruud Gullit'
vanbasten = 'Marco van Basten' 

#2.
goal_0 = 32
goal_1 = 54

#4
report = gullit + ' scored in the ' + str(goal_0) + 'nd minute\n' + vanbasten + ' scored in the ' + str(goal_1) + 'th minute'
report_1 = f'{gullit} scored in the {goal_0}nd minute\n{vanbasten} scored in the {goal_1}th minute' #ALTERNATIVE to [report] with f'{}

# PART 2
#1.
player = 'Ruud Gullit'

#2.
first_name = player[:player.find(' ')]

#4.
name_short = player[:1] + ". " + player[player.find(' ')+1:]
print(name_short)
name_short1 = f'{player[:1]}. {player[player.find(" ")+1:]}' #ALTERNATIVE to [name_short] with f'{}
print(name_short1)
name_short2 = player[0].upper() + ". " + player[player.find(' ')+1:]
print(name_short2)


#5.
chant = (first_name + "! ") * (len(first_name) - 1) + (first_name + "!")
# chant1 = f'{first_name}! ' * (len(first_name) - 1) and f'{first_name}!' => This does not work. Only prints 'Ruud!'. Code stops after the second accolade, behind the first exclamation mark.
print(chant)



