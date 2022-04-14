import os


def simple_words():

    path = os.getcwd().rsplit("/", 1)[0] + "/acceptor_dummy/simple_words.syms"
    with open(path, "w+") as f:
        f.write("<epsilon>" + "\t" + " 0" + "\n")
        f.write("theo" + "\t 1 \n")
        f.write("theodore" + "\t" + " 2" + "\n")
        f.write("thodo" + "\t" + " 3" + "\n")
        f.write("thodoris" + "\t" + " 4" + "\n")
        
        
if __name__=="__main__":
    simple_words()
