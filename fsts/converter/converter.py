import os
import string


def edit_distance_converter():
    """Write in a file all the transitions for the levenshtein distance. The form of a line is 0 0 (the converter has only one state) let_i let_j num_k, where num_k is either 0 or 1. Then we iterate 
       over the ascii lowercase symbols and adjust the weights as requested. """

    # print(write_dir)  # /home/thodoris/Desktop/lab/fsts/converter/model.txt
    with open("L.fst", "a") as f:
        
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
