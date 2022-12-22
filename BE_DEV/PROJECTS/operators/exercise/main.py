# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

#1
spain_language_main = 'Spanish'
switzerland_language_main = 'German'
print(spain_language_main is switzerland_language_main)

#2
spain_religion_main = 'Roman Catholic'
switzerland_religion_main = 'Roman Catholic'
print(spain_religion_main is switzerland_religion_main)

#3
spain_capital = 'Madrid'
switzerland_capital = 'Bern'
print(len(spain_capital) != (len(switzerland_capital)))

#4
spain_gdp_2020 = 1714860000000
switzerland_gdp_2020 = 590710000000
print(switzerland_gdp_2020 > spain_gdp_2020)

#5
spain_pop_growth = 0.13
switzerland_pop_growth = 0.65
print(spain_pop_growth < 1 and switzerland_pop_growth < 1)

#6
spain_pop_2022 = 47163418
switzerland_pop_2022 = 8508698
print((spain_pop_2022 or switzerland_pop_2022) > 10000000)

#7
print((spain_pop_2022 > 10000000 and switzerland_pop_2022 < 10000000) or (spain_pop_2022 < 10000000 and switzerland_pop_2022 > 10000000))
