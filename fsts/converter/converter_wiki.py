import os
import string
import numpy as np


def edit_distance_converter():
    """Write in a file all the transitions for the levenshtein distance. The form of a line is 0 0 (the converter has only one state) let_i let_j num_k, where num_k is either 0 or 1. Then we iterate 
       over the ascii lowercase symbols and adjust the weights as requested. """

    # print(write_dir)  # /home/thodoris/Desktop/lab/fsts/converter/model.txt
    with open("N.fst", "a") as f:

        np.random.seed(7)

        path = os.getcwd().rsplit("/", 2)[0] + "/data/wiki.txt"

        with open(path, "r+") as f:

            lines = list(f.readlines())
            
            num_rows = sum(1 for line in lines)
            
            rnd_int = np.random.randint(num_rows)
        
            rnd_line = lines[rnd_int]

        correct_word = rnd_line.split("\t")[1].split("\n")[0]
        
        for l_1 in string.ascii_lowercase:
            for l_2 in string.ascii_lowercase:
                # different letter transitions with weight 1
                if l_2 != l_1:
                    f.write("0 0 " + l_1 + " " + l_2 + " 1")
                    f.write("\n")
                    
                # same letter transitions with zero weight
                else:
                    f.write("0 0 " + l_1 + " " + l_1 + " 0")
                    f.write("\n")
        # eps to letter and letter to eps transitions with weight 1
        for letter in string.ascii_lowercase:
            f.write("0 0 " + "<epsilon>" + " " + letter + " 1")
            f.write("\n")
            f.write("0 0 " + letter + " " + "<epsilon>" + " 1")
            f.write("\n")
            
        # consider 0 as a final state
        f.write("0")
        
    
if __name__=="__main__":
    edit_distance_converter()

