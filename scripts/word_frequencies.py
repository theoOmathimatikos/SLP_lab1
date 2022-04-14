import os
from collections import Counter


def value_counts(read_path, write_path):
    """This function saves a dictionary in a text file, by writing its keys and values in a key +\t + value form. We read all words of all lines from the text file that we saved the cleaned corpus
       and then put them in a list. The Counter object from the collections takes this list and produces a dictionary with the tokens and their occurrences. We then exclude all words with a count
       less than 5. At last, we save the dictionary, by writing its key:value pairs (separated by tab) in different lines of a txt file."""
    
    # find the directory in which to write the words.vocab text file
    cwdir = os.getcwd()
    write_dir = cwdir.rsplit("/", 1)[0] + "/" + write_path
    read_dir = cwdir.rsplit("/", 1)[0] + "/" + read_path
    
    # get the text file
    file1 = open(read_dir, 'r')
    lines = file1.readlines()
    file1.close()
    
    # use Counter to speed up the code.
    words = []
    for line in lines:
        words.extend(line.split(" "))
    word_freq = Counter(words)
    
    # print 10 most common words
    print(word_freq.most_common(10))
    
    print("Before excluding rare tokens, the dictionary had length:", len(list(word_freq.keys())))
    # Exclude words that appear less than 5 times.
    word_freq = {k:v for (k, v) in list(word_freq.items()) if v >= 5}
    print("After excluding rare tokens, the dictionary has length:", len(list(word_freq.keys())))
    
    # write the results in a tab separated txt file
    with open(write_dir, 'w+') as f:
        for k, v in list(word_freq.items()):
            if len(k) >= 1 and k != "\n":
                f.write(k + "\t" + str(v) + "\n")
    return
    
   
if __name__ == "__main__":
    read_path = "data/preprocessed_sentences.txt"
    write_path = 'vocab/words.vocab.txt'
    value_counts(read_path, write_path)
   
