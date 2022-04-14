import os 


def word_to_index(read_path, write_path):
    """This function creates a syms tab-separated file, with two columns. The first contains the key, which corresponds to a word in our vocabulary (in the words.vocab.txt), and the second contains
       the value, that corresponds to a unique index. The indices result from an index that starts from zero and increases by one in each iteration. The first line of the file that we read corresponds
       to the header, and thus, is been neglected."""
    
    # find file directories to read and save files
    cwdir = os.getcwd()
    read_dir = cwdir.rsplit("/", 1)[0] + "/" + read_path
    write_dir = cwdir.rsplit("/", 1)[0] + "/" + write_path
    
    f = open(read_dir)
    g = open(write_dir, "w+")
    
    # write in the g file
    lines = f.readlines()
    g.write("<epsilon> " + "\t" + "0" + "\n")
    for i in range(1, len(lines)):
        line = lines[i]
        word = line.split("\t")[0]
        g.write(word + "\t" + str(i) + "\n")
        
    f.close()
    g.close()


if __name__ == '__main__':
    read_path = 'vocab/words.vocab.txt'
    write_path = 'vocab/words.syms'
    word_to_index(read_path, write_path)

