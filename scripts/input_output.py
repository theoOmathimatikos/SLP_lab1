import os
import string


def input_output_file(write_path):
    """This function creates a syms tab-separated file, with two columns. The first contains the key, which corresponds to the letter, and the second contains the value, that corresponds to a
    unique index. The indices result from an index that starts from zero and increases by one in each iteration. We iterate over the lowercase letters, but first we add the <eps> symbol."""
    
    # find file directory to save the file
    cwdir = os.getcwd()
    write_dir = cwdir.rsplit("/", 1)[0] + "/" + write_path

    # write the letters-indices, with the <eps> first. 
    with open(write_dir, "w+") as f:
        f.write("<eps>" + "\t" + str(0) + "\n")
        for i, letter in enumerate(string.ascii_lowercase):
            f.write(letter + "\t" + str(i+1) + "\n")

    return


if __name__ == '__main__':
    write_path = 'vocab/chars.syms'
    input_output_file(write_path)

