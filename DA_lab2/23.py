import numpy as np
f = open('frequency.txt', encoding="utf-8")
s = f.read()
list_word = s.split('\n')
# for i in range(len(list_word)):
    # count = list_word[i].find(' ')
    # list_word[i] = list_word[i][:count]
open('estimations.txt', 'w').close()
f2 = open('estimations.txt', 'a', encoding='utf-8')
for i in range(101, len(list_word)):
        f2.write(str(list_word[i]) + " " + str(np.random.randint(-1, 2)) + "\n")