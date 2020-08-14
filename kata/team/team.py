# http://codeforces.com/problemset/problem/231/A

list_a = [1, 1, 0]
list_b = [1, 1, 1]
list_c = [1, 0, 0]
input_list = [list_a, list_b, list_c]

amount_of_solved = 0

for loop_list in input_list:

    amount_sure = 0

    for answers in loop_list:
        if answers == 1:
            amount_sure += 1
    if amount_sure > 1: amount_of_solved += 1

print(amount_of_solved)
