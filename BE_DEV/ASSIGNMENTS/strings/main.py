# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# UEFA EURO 1988 FINAL

# PART 1

#1.
gullit = 'Ruud Gullit'
vanbasten = 'Marco van Basten' 

#2.
goal_0 = 32
goal_1 = 54

#3.
scorers = gullit + ' ' + str(goal_0) + ', ' + vanbasten + ' ' + str(goal_1)

#4.
report = gullit + ' scored in the ' + str(goal_0) + 'nd minute\n' + vanbasten + ' scored in the ' + str(goal_1) + 'th minute'

# PART 2

#1.
player = 'Ruud Gullit'

print(len(player))

#2.
first_name = player[:player.find(' ')]
print(first_name)

#3.
last_name_len = len(player[player.find(' ')+1:])
print(last_name_len)


#4.
name_short = player[:1] + ". " + player[player.find(' ')+1:]
print(name_short)

#5.
chant = (first_name + "! ") * (len(first_name) - 1) + (first_name + "!")
print(chant)

#6.
good_chant = (chant[:-1] != ' ')
print(good_chant)
