# http://codeforces.com/problemset/problem/158/A

nth_finisher = 5
score_list = [10, 9, 8, 7, 7, 7, 5, 5]
score = score_list[nth_finisher - 1]
advancers = 0

for number in score_list:
    if number >= score:
        advancers += 1

print(advancers)