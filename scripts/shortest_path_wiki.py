import os 
import numpy as np
def find_path():

    path = os.path.join(os.getcwd(), 'wiki.txt')

    wiki = np.loadtxt(path, dtype=str)

    for line in wiki:

        wrong_word, correct_word = line[0], line[1]

        with open(os.getcwd() + '/temp_wiki.txt', 'w+') as g:

            g.write(wrong_word)
            g.write(' ')
            g.write(correct_word)

        os.system('bash ./shortest_path.sh $(cat temp_wiki.txt) >>  wiki_shortest_path.txt')
        os.system(" echo '\n' >> wiki_shortest_path.txt")

        os.system('bash ./word_edits.sh $(cat temp_wiki.txt) >>  edits.txt')
        os.system(" echo '\n' >> edits.txt")

    os.system('rm temp_wiki.txt')


if __name__ == '__main__':
    find_path()
