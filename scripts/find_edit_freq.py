from collections import Counter
import os
import numpy as np

def edit_freq():
    

        with open(os.getcwd() + '/edits.txt', 'r+') as f:
            lines = f.readlines()

        lines = [(line.strip()).replace('\t', ' ') for line in lines]

        count = Counter(lines)
        del count['']

        total_freq = sum(count.values())

        count = dict([(key, np.round(value/total_freq, 4)) for key, value in count.items()])

        with open((os.getcwd() + '/edits_freq.txt'), 'w+')as g:

            for key in count:
            
                g.write(str(key))
                g.write(' ')
                g.write(str(count[key]))
                g.write('\n')


if __name__ == '__main__' :

    edit_freq()
