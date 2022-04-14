import os
import string
import numpy as np
import math

INFINITY = 1000000000

def edit_distance_converter():
    """Write in a file all the transitions for the levenshtein distance. The form of a line is 0 0 (the converter has only one state) let_i let_j num_k, where num_k is either 0 or 1. Then we iterate 
       over the ascii lowercase symbols and adjust the weights as requested. """


    with open(os.getcwd().rsplit('/', 2)[0] + '/scripts/edits_freq.txt', 'r+') as g:
    
        lines = g.readlines()

        lines = [line.strip() for line in lines]
        lines = dict([((line.split(' ')[0], line.split(' ')[1]), float(line.split(' ')[2])) for line in lines])

    with open("E.fst", "w+") as f:
        
        for l_1 in string.ascii_lowercase:
            for l_2 in string.ascii_lowercase:
                # different letter transitions with weight 1
                if (l_1, l_2) in lines.keys():
                    f.write("0 0 " + l_1 + " " + l_2 + " " + str(-math.log(lines[l_1, l_2])))
                    f.write("\n")
                    
                # same letter transitions with zero weight
                else:
                    f.write("0 0 " + l_1 + " " + l_2 + " " + str(INFINITY))
                    f.write("\n")
        # eps to letter and letter to eps transitions with weight 1
        for letter in string.ascii_lowercase:
            if ('<epsilon>', letter) in lines.keys():
                f.write("0 0 " + "<epsilon>" + " " + letter + " " + str(-math.log(lines['<epsilon>', letter])))
                f.write("\n")

            elif (letter, '<epsilon>') in lines.keys():
                f.write("0 0 " + letter + " " + "<epsilon>" + " " + str(-math.log(lines[letter, '<epsilon>'])))
                f.write("\n")

            else:
                f.write("0 0 " + "<epsilon>" + " " + letter + " " + str(INFINITY))
                f.write("\n")

                f.write("0 0 " + letter + " " + "<epsilon>" + " " + str(INFINITY))
                f.write("\n")

        # consider 0 as a final state
        f.write("0")
        
    
if __name__=="__main__":
    edit_distance_converter()
