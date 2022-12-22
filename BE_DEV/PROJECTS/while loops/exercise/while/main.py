from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# 1 unique_koala_fact

def unique_koala_facts(int):


    facts_list = []
    unique_facts = []

    while int in range(1000):
        facts_list.append(random_koala_fact())
        int -= 1
    else:
        for fact in facts_list:
            if fact not in unique_facts:
                unique_facts.append(fact)
            continue
    return unique_facts

# 2 num_joey_facts

def num_joey_facts():

    fact_check = random_koala_fact()
    fact_list = []
    unique_joey_facts = []
    fact_counter = 0
    joey_counter = 0
    joey = "joey"

    while fact_counter < 10:
        fact_list.append(random_koala_fact())
        if random_koala_fact() == fact_check:
            fact_counter += 1
  
    for facts in fact_list:
        if joey in facts and facts not in unique_joey_facts:
            unique_joey_facts.append(facts)
            joey_counter += 1

    return joey_counter

# 3 koala_weight

def koala_weight():

    weight = 0
    while weight == 0:
        fact = random_koala_fact()
        if 'kg' in fact: 
            weight += int(fact[fact.find("kg")-2:fact.find('kg')])
        continue
    return (weight)


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(random_koala_fact())
    print(unique_koala_facts(5))
    print(num_joey_facts())
    print(koala_weight())
