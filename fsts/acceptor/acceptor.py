import os


def accept():
    """ This function creates a FSA with an initial state 0 and an accept state 1. For every word w of our corpus, it creates a path of states Q_w1, ..., Q_wn. The initial state 0 is connected to the
     state Q_w1 through an <eps> transition and we move from Q_wi to Q_w{i+1} only if we read the i-th letter of the word w. At last, we add a transition from the state Q_wn to the final state 1,
     only if we read the last letter of w. Thus, we have created for every word a path that leads to the final state and can be accessed through an <eps> transition. If an input word belongs to the
     corpus, it will randomly find the corresponding path of the word and lead to the accepting state, whereas if it does not, it will get stuck to some intermediary state. A counter is increased by
     one, every time a new state is created, so as we do not try to create a new state that its name already exists. 
     
     We rely upon the different methods of the fst module, in order to make our model simpler. 
     """

    path = os.getcwd().rsplit("/", 1)[0] + "/acceptor/words.syms"
    with open(path, "r+") as f:
        lines = f.readlines()

    i = 1
    S = set()

    init_state = 0
    with open("V.fst", "w+") as g:
        for line in lines:
            word = line.split("\t")[0]
            if word.startswith("<epsilon>"):
                continue

            # create a path of states for a word, only once
            if word not in S:
                S.add(word)
                for j in range(len(word)):
                    # transfer from the inital state to the first state of this word
                    if j == 0:
                        g.write(str(init_state) + " " + str(i) + " <epsilon>" + " " + "<epsilon>" + " 0")
                        g.write("\n")

                        g.write(str(i) + " " + str(i + 1) + " " + word[j] + " " + "<epsilon>" + " 0")
                        g.write("\n")
                        i += 1

                    # transfer to the accept state 1, return the word?
                    elif j == len(word) - 1:
                        g.write(str(i) + " " + str(i + 1) + " " + word[j] + " " + word + " 0")
                        g.write("\n")
                        g.write(str(i + 1))
                        g.write("\n")

                        i += 2
                        break

                    # one letter step for a word
                    else:
                        g.write(str(i) + " " + str(i + 1) + " " + word[j] + " " + "<epsilon>" + " 0")
                        g.write("\n")
                        i += 1

    return


if __name__=="__main__":
    accept()
