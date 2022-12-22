# Do not modify these lines
__winc_id__ = '63ce21059cf34d3d8ffef497ede7e317'
__human_name__ = 'comments'

# Add your code after this line

# Groceries at a supermarket
products = ['Broccoli', 'Leek', 'Potato', 'Brussel Sprouts']

print(products)

products[0] = 2.00 # Price per kg in euros
products[1] = 2.00 # Price per kg in euros
products[2] = 3.00 # Price per kg in euros
products[3] = 7.00 # Price per kg in euros

# The total value of one kilo of each product in euros
sum_one_each = (products[0] + products[1] + products[2] + products[3])

print(sum_one_each)

avg_price = "The average price per kilo in euros is {0:.2f}".format (sum_one_each / len(products))

print(avg_price)

"""By using these strings of code the amount of products can be counted, by eventually the use of len(products). Therefor the amount, in this case 4, does not need be assigned manually."""

# The amount of kilos selected per product
num_broccolis = 5
num_leeks = 2
num_potatoes = 7
num_brussel_sprouts = 10

# The sum of the order in euros
sum_total = num_broccolis * products[0] + num_leeks * products[1] + num_potatoes * products[2] + num_brussel_sprouts * products[3]   

print(sum_total)

discount_percentage = 30 # Value can be adjusted accordingly without the need to change the formula below

discounted_value = sum_total / 100.00 * discount_percentage

print(discounted_value)

discounted_sum_total = sum_total - discounted_value

print(discounted_sum_total)

"""Fun little experience to use different, slightly more advanced code to reach the same result for the previous exercise Calculate."""
