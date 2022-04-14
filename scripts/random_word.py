import os
import numpy as np

np.random.seed(7)

path = os.getcwd().rsplit("/", 1)[0] + "/data/wiki.txt"
with open(path, "r+") as f:

    lines = list(f.readlines())
    
    num_rows = sum(1 for line in lines)
    
    rnd_int = np.random.randint(num_rows)

    rnd_line = lines[rnd_int]


wrong_word = rnd_line.split("\t")[0].split("\n")[0]
correct_word = rnd_line.split("\t")[1].split("\n")[0]

with open('words_wiki.txt', 'w+') as e:
    e.write(wrong_word)
    e.write(' ')
    e.write(correct_word)
