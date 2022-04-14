import glob
import os
import re

import numpy as np
from sklearn import model_selection, linear_model, metrics

import contractions
from gensim.models import Word2Vec, KeyedVectors
from w2v_train import W2VLossLogger


SCRIPT_DIRECTORY = os.path.realpath(__file__)

data_dir = "../data/aclImdb/"      # os.path.join(SCRIPT_DIRECTORY, "../data/aclImdb/")
train_dir = os.path.join(data_dir, "train")
test_dir = os.path.join(data_dir, "test")
pos_train_dir = os.path.join(train_dir, "pos")
neg_train_dir = os.path.join(train_dir, "neg")
pos_test_dir = os.path.join(test_dir, "pos")
neg_test_dir = os.path.join(test_dir, "neg")

# For memory limitations. These parameters fit in 8GB of RAM.
# If you have 16G of RAM you can experiment with the full dataset / W2V
MAX_NUM_SAMPLES = 5000
# Load first 1M word embeddings. This works because GoogleNews are roughly
# sorted from most frequent to least frequent.
# It may yield much worse results for other embeddings corpora
NUM_W2V_TO_LOAD = 1000000


SEED = 42

# Fix numpy random seed for reproducibility
np.random.seed(SEED)


def strip_punctuation(s):
    s = contractions.fix(s)  # this is compulsory if we don't want some words that are in the text not to be excluded. 
    return re.sub(r"[^a-zA-Z\s]", " ", s)


def preprocess(s):
    return re.sub("\s+", " ", strip_punctuation(s).lower())


def tokenize(s):
    return s.split(" ")


def preproc_tok(s):
    return tokenize(preprocess(s))


def read_samples(folder, preprocess=lambda x: x):

    samples = glob.iglob(os.path.join(folder, "*.txt"))
    data = []

    for i, sample in enumerate(samples):
        if MAX_NUM_SAMPLES > 0 and i == MAX_NUM_SAMPLES:
            break
        with open(sample, "r") as fd:
            x = [preprocess(l) for l in fd][0]
            data.append(x)

    return data


def create_corpus(pos, neg):

    corpus = np.array(pos + neg)
    y = np.array([1 for _ in pos] + [0 for _ in neg])
    indices = np.arange(y.shape[0])
    np.random.shuffle(indices)
    # We do this so as we do not want our model to learn any pattern in the sequence of the data.?

    return list(corpus[indices]), list(y[indices])


def load_model():
    """This function loads the pretrained and saved model from the models folder. It will then it. """
    output_file = os.getcwd().rsplit("/", 1)[0] + "/models/gutenberg_w2v.100d.model"
    print(output_file)
    model = Word2Vec.load(output_file)
    
    return model
    

def load_pretrained_model():
    """This function loads a pretrained model from google and then returns it. """

    read_dir = os.getcwd().rsplit("/", 1)[0] + "/" 'data/GoogleNews-vectors-negative300.bin'
    model = KeyedVectors.load_word2vec_format(read_dir, binary=True, limit=100000)
    return model


def nbow_value(nbow, load, exclude_zeros=False):
    """ This method receives for every text the corresponding 100-D representations of the words of the text, and
    returns the mean value of those representations, calculated at the 0 axis"""
    estim = []
    for lst in nbow:
        arr = np.array(lst)
        if load:
            arr = np.vstack(lst)
        if exclude_zeros:
            estim.append(np.mean(arr[arr.any(axis=1)], axis=0))
        else:
            estim.append(np.mean(arr, axis=0))
    return estim
        

def extract_nbow(corpus, load_simple=True, exclude_zeros=False):
    """Extract neural bag of words representations. For each text, we tok"""
    if load_simple:
        model = load_model()
        n = 100
    else:
        model = load_pretrained_model()
        n = 300
    nbow = []
    for text in corpus:
        rep = []
        for word in text:
            try:
                rep.append(model.wv[word])
            except:
                rep.append(np.zeros(n))
        nbow.append(rep)
    estim = nbow_value(nbow, load_simple, exclude_zeros)
    estim = np.array(estim)

    return estim
    

def train_sentiment_analysis(train_corpus, train_labels):
    """Train a sentiment analysis classifier using NBOW + Logistic regression"""
    clf = linear_model.LogisticRegression(solver='liblinear', random_state=0).fit(train_corpus, train_labels)
    return clf


def evaluate_sentiment_analysis(classifier, test_corpus, test_labels):
    """Evaluate classifier in the test corpus and report accuracy. The metrics used are the accuracy of the model and
    the confusion matrix."""
    print("The accuracy of the model is:", classifier.score(test_corpus, test_labels))
    print("Confusion Matrix")
    print(metrics.confusion_matrix(test_labels, classifier.predict(test_corpus)))


if __name__ == "__main__":
    
    # Read Imdb corpus
    
    # load the positive and negative texts, with the use of read_samples. Thus, the returned text is cleaned. 
    positive = []
    negative = []
    for find_dir in [pos_train_dir, pos_test_dir]:
        new_data = read_samples(find_dir, preproc_tok)
        positive.extend(new_data)
    for find_dir in [neg_train_dir, neg_test_dir]:
        new_data = read_samples(find_dir, preproc_tok)
        negative.extend(new_data)
    
    # create a corresponding labeling list and randomly shuffle the corpus and the labels. 
    corpus, labels = create_corpus(positive, negative)
    
    # from the text corpus to a list with a single number for each text. 
    nbow_corpus = extract_nbow(corpus, True, exclude_zeros=False)
    print(nbow_corpus.shape)
    (
        train_corpus,
        test_corpus,
        train_labels,
        test_labels,
    ) = model_selection.train_test_split(nbow_corpus, labels, test_size=0.2)

    print(train_corpus.shape)
    print(test_corpus.shape)

    # train / evaluate and report accuracy
    clf = train_sentiment_analysis(train_corpus, train_labels)
    evaluate_sentiment_analysis(clf, test_corpus, test_labels)
