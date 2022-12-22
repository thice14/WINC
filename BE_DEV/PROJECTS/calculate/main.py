# Do not modify these lines
__winc_id__ = '499e67d5cb54448e93cee7465be2c866'
__human_name__ = 'calculate'

# Add your code after this line

#1
broccoli = 2.00 # You can also use float(2) notation. You need one of either option to calculate a % later on
leek = 2.00
potato = 3.00
brussel_sprout = 7.00

#2
sum_one_each = (broccoli + leek + potato + brussel_sprout)

#3
total_num_products = len('broccoli leek potato brussel_sprout'.split())
total_num_products2 = len(['broccoli', 'leek', 'potato', 'brussel_sprout']) # (Better) alternative

avg_price = (sum_one_each / total_num_products) # Instead of (sum_one_each / 4.0)

#4
num_potatoes = 7
num_broccolis = 5
num_leeks = 2
num_brussel_sprouts = 10

#5
sum_total = (num_potatoes * potato + num_broccolis * broccoli + num_leeks * leek + num_brussel_sprouts * brussel_sprout)

#6
discount_percentage = 30.00

#7
discounted_value = sum_total / 100 * discount_percentage

discounted_sum_total = sum_total - discounted_value

print(discounted_sum_total)

discounted_sum_total2 = sum_total - sum_total / 100 * discount_percentage # One phrase alternative, no need to create value [discount_value]