import re
import sys
import os
from tkinter import NW
import string
import contractions
import nltk


def download_corpus(corpus="gutenberg"):
    """Download Project Gutenberg corpus, consisting of 18 classic books

    Book list:
       ['austen-emma.txt',
        'austen-persuasion.txt',
        'austen-sense.txt',
        'bible-kjv.txt',
        'blake-poems.txt',
        'bryant-stories.txt',
        'burgess-busterbrown.txt',
        'carroll-alice.txt',
        'chesterton-ball.txt',
        'chesterton-brown.txt',
        'chesterton-thursday.txt',
        'edgeworth-parents.txt',
        'melville-moby_dick.txt',
        'milton-paradise.txt',
        'shakespeare-caesar.txt',
        'shakespeare-hamlet.txt',
        'shakespeare-macbeth.txt',
        'whitman-leaves.txt']
    """
    nltk.download(corpus)
    raw = nltk.corpus.__getattr__(corpus).raw()

    return raw


def identity_preprocess(s):
    return s


def clean_text(s):
    s = s.strip()  # The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space: default leading character to remove)
    s = s.lower()  # convert to lowercase
    s = contractions.fix(s)  # e.g. don't -> do not, you're -> you are
    s = re.sub("\s+", " ", s)  # strip multiple whitespace
    s = re.sub(r"[^a-z\s]", " ", s)  # keep only lowercase letters and spaces

    return s


def tokenize(s):
    tokenized = [w for w in s.split(" ") if len(w) > 0]  # Ignore empty string
    return tokenized


def preprocess(s):
    return tokenize(clean_text(s))


def process_file(corpus, preprocess=identity_preprocess):
    # Check if a stop is in an acronym
    def stop_in_acronym(corpus, index):

        if corpus[index] == ".":

            if index == len(corpus) - 1:
                return True

            j = 1
            while corpus[index - j] not in [" ", ".", "\n"]:
                j += 1
            first_word = corpus[index - j + 1:index]
            if first_word in ["mr", "mrs", "Mr", "Mrs", '"Mr', '"mr', '"Mrs', '"mrs']:
                return True

            if (len(first_word) == 1) and (corpus[index - j] == '.'):
                return True

            k = 1
            while index + k < len(corpus) and corpus[index + k] not in [" ", ".", "\n"] :
                k += 1
            second_word = corpus[index + 1:index + k]
            if len(first_word) == 1 and len(second_word) == 1:
                return True
            else:
                return False
        else:
            return False

    def apostrophe_in_word(corpus, index):

        if corpus[index] == '\'':
            
            is_letter_before = corpus[index -1] in string.ascii_lowercase or corpus[index -1] in string.ascii_uppercase 
            is_letter_after = corpus[index + 1] in string.ascii_lowercase

            return is_letter_before and is_letter_after

    # filter out acronym stops
    new_corpus = [corpus[i] for i in range(len(corpus)) 
        if not (stop_in_acronym(corpus, i) or apostrophe_in_word(corpus, i))]
    new_corpus = ''.join(new_corpus)
    
    # Every other stop means a sentence
    if corpus == 'guttenberg':
        splitted_corpus = re.split('\.|\n\n', new_corpus)
    else:
        # Split after new line if it is preceded by capital letters
        splitted_corpus = re.split('\.|(?<=[A-Z])\n', new_corpus)

    lines = [preprocess(ln) for ln in splitted_corpus]
    lines = [ln for ln in lines if len(ln) > 0]  # Ignore empty lines

    return lines


if __name__ == "__main__":

    CORPUS = sys.argv[1] if len(sys.argv) > 1 else "gutenberg"
    raw_corpus = download_corpus(corpus=CORPUS)

    preprocessed = process_file(raw_corpus, preprocess=preprocess)
    
    cwdir = os.getcwd()
    write_dir = cwdir.rsplit("/", 1)[0] + "/" + "data/preprocessed_sentences.txt"
    f = open(write_dir, "a")	
    for sentence in preprocessed:
        if sentence[0] in ["volume", "chapter"] and len(sentence) < 5:
            continue
        for word in sentence:
            f.write(word + " ")
        f.write("\n")
    f.close() 
    
