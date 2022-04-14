import sys
sys.path.insert(0, '/home/thodoris/Desktop/lab/scripts/')
import util
import os


def neg_logarithm():
    
    path = os.getcwd().rsplit("/", 2)[0] + "/vocab/words_frequencies.vocab.txt"
    with open(path, "r+") as f:
        lines = f.readlines()
    
    with open('negative_log_acceptor.txt', "w+") as g:
        for line in lines:
            word, freq = line.split("\t")
            g.write("0 0 " + word + " " + word + " " + str(util.calculate_arc_weight(float(freq))))
            g.write("\n")
        g.write("0")
        
        
if __name__ == "__main__":
    neg_logarithm()
