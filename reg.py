import shuntingYard
import thompson

with open('text.txt', 'r') as f:
    list_of_lists = []
    for line in f:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        list_of_lists.append(line_list)
    print(list_of_lists)
    

for test in list_of_lists:
    infix = test[0]
    i = 1
    print(f"infix:  {infix}")
    postfix = shuntingYard.shunt(infix)
    print(f"postfix: {postfix}")
    nfa = thompson.re_to_nfa(postfix)
    print(f"thompson: {nfa}")
    # loop through list
    while test:
        s = test[i]
        match = nfa.match(s)
        print(f"Match '{s}': {match}")
        # if list matches end then end of list
        if test[i] == test[-1]:
            break
        i+=1
    print()