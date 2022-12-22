from helpers import random_koala_fact

unique_koala_facts = 0
fact_counter = 0
fact_list = []
unique_fact_list = []

while fact_counter < 1000:
    fact_list.append(random_koala_fact())
    fact_counter += 1
else:
    for fact in fact_list:
        if fact not in unique_fact_list:
            unique_fact_list.append(fact)
            unique_koala_facts += 1
        continue

# Answer: There are 29 unique koala facts in the list

def unique_koala_facts(int):

    unique_koala_fact = 0
    fact_counter = 0
    fact_list = []
    unique_fact_list = []

    while int in range(0,1000):
        fact_list.append(random_koala_fact())
        fact_counter += 1
        int -= 1
    else:
        for fact in fact_list:
            if fact not in unique_fact_list:
                unique_fact_list.append(fact)
                unique_koala_fact += 1
            continue
    return unique_koala_fact

