import os
from gensim.models import Word2Vec
from w2v_train import W2VLossLogger


def save_embeddings():
    """This method first reads the data and loads our pretrained model. Then it creates two new files, the metadata.tsv and the embeddings.tsv, where it 
    writes the words of the corpus in the first one, and the corresponding epbeddings on the second."""
    # read the data
    path = os.getcwd().rsplit("/", 1)[0] + "/vocab/words.vocab.txt"
    with open(path, "r+") as f:
        lines = f.readlines()
    
    # load model
    output_file = os.getcwd().rsplit("/", 1)[0] + "/models/gutenberg_w2v.100d.model"
    model = Word2Vec.load(output_file)
    
    # find the embeddings of each word and save it 
    f1 = open("metadata.tsv", "w+")
    f2 = open("embeddings.tsv", "w+") 
    for line in lines:
        word = line.split("\t")[0]
        try:
            embeddings = model.wv[word]
            f1.write(word+"\n")
            for i in embeddings:
                f2.write(str(i) + "\t")
            f2.write("\n")
        except KeyError:
            print("Word", word, "not in vocabulary.")


if __name__=="__main__":
    save_embeddings()
