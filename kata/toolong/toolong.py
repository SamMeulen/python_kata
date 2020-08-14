# http://codeforces.com/problemset/problem/71/A

wordlist = ["word", "localization", "internationalization", "pneumonoultramicroscopicsilicovolcanoconiosis"]

for word in wordlist:
    print(word) if len(word) < 11 else print(word[0] + str(len(word)-2) + word[len(word) - 1])
