def eligible_to_vote(age, nationality):
    if age >= 18:
        if nationality == 'Italian':
            return True
        else:
            return False
    else:
        return False

def eligible_to_vote(age, nationality):
    if age >= 18 and nationality == 'Italian':
        return True
    else:
        return False

def eligible_to_vote(age, nationality):
    if age >= 18 and nationality == 'Italian':
        return True
    return False

def eligible_to_vote(age, nationality):
    if age >= 18 and nationality == 'Italian':
        print('Bene!')
        return True
    elif age >= 25 and nationality == 'Portuguese':
        print('Sim!')
        return True
    elif age >= 31 and nationality == 'Dutch':
        print('Top!')
        return True
    elif age >= 19 and nationality == 'Malawian':
        print('Iya!')
        return True
    else:
        return False   

"""An if statement with elif clauses uses short-circuit evaluation, 
analogous to what you saw with the and and or operators. 
Once one of the expressions is found to be true and its block is executed, 
none of the remaining expressions are tested."""

debugging = True  # Set to True to turn debugging on.

if debugging: print('About to call function foo()')
