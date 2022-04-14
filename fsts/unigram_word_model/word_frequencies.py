import os

def find_frequencies():

    path = os.getcwd().rsplit("/", 2)[0] + "/vocab/words.vocab.txt"
    with open(path, "r+") as f:
        lines = f.readlines()
    
    
    tot = 0
    for line in lines: 
        tot += int(line.split("\t")[1])
        
    with open(path.rsplit("/", 1)[0] + "/words_frequencies.vocab.txt", "w+") as g:
    	for line in lines:
    	    word, num_occurences = line.split("\t")[0:2]
    	    num_occurences = int(num_occurences)
    	    g.write(word + "\t" + str(num_occurences/tot) + "\n")
        
        
if __name__=="__main__":
    find_frequencies()
