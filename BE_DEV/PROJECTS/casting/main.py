# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

# PART 1

#1
leek_price = int(2)

#2
print('Leek is ' + str(leek_price) + ' euro per kilo.')

# PART 2

#1
order = 'leek 4'

#2
amount = order[order.find(' ')+1:]

#3
real_amount = int(amount)

#4
sum_total = leek_price * real_amount
print(sum_total)

# PART 3

#1
broccoli_price = 2.34
order = 'broccoli 1.6'

#2
order_amount = float(order[order.find(' ')+1:])
total_price_broccoli = round(broccoli_price * order_amount,2)

#3
print(str(order_amount) + 'kg broccoli costs ' + str(total_price_broccoli) + 'e')










