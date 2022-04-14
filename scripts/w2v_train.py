import logging
import multiprocessing
import os

from gensim.models import Word2Vec, KeyedVectors
from gensim.models.callbacks import CallbackAny2Vec

# Enable gensim logging
logging.basicConfig(
    format="%(levelname)s - %(asctime)s: %(message)s",
    datefmt="%H:%M:%S",
    level=logging.INFO,
)


class W2VLossLogger(CallbackAny2Vec):
    """Callback to print loss after each epoch
    use by passing model.train(..., callbacks=[W2VLossLogger()])
    """

    def __init__(self):
        self.epoch = 0

    def on_epoch_end(self, model):
        loss = model.get_latest_training_loss()

        if self.epoch == 0:
            print("Loss after epoch {}: {}".format(self.epoch, loss))
        else:
            print(
                "Loss after epoch {}: {}".format(
                    self.epoch, loss - self.loss_previous_step
                )
            )
        self.epoch += 1
        self.loss_previous_step = loss


def train_w2v_model(
    sentences,
    output_file,
    window=5,
    embedding_dim=100,
    epochs=300,
    min_word_count=10,
):
    """Train a word2vec model based on given sentences.
    Args:
        sentences list[list[str]]: List of sentences. Each element contains a list with the words
            in the current sentence
        output_file (str): Path to save the trained w2v model
        window (int): w2v context size
        embedding_dim (int): w2v vector dimension
        epochs (int): How many epochs should the training run
        min_word_count (int): Ignore words that appear less than min_word_count times
    """
    workers = multiprocessing.cpu_count()

    # Instantiate gensim.models.Word2Vec class
    model = Word2Vec(sentences=sentences, size=embedding_dim, window=window, min_count=min_word_count, workers=workers)
    
    # Train word2vec model
    model.train(sentences, epochs=epochs, total_examples=len(sentences), callbacks=[W2VLossLogger()])
    
    # Save trained model
    model.save(output_file)

    return model


def load_model(output_file):
    """This function loads the pretrained and saved model from the models folder. It will then call the model_stats
    function and return its results. """
    # load the model
    model = Word2Vec.load(output_file)
    return model_stats(model)


def load_pretrained_model():
    """This function loads a pretrained model from google and thens call the model_stats function, returns
    its results. """
    
    # Read the data
    read_dir = os.getcwd().rsplit("/", 1)[0] + "/" 'data/GoogleNews-vectors-negative300.bin'
    # load the model
    model = KeyedVectors.load_word2vec_format(read_dir, binary=True, limit=100000)
    return model_stats(model)


def model_stats(model):
    """This function takes as an input a Word2Vec model and makes some predictions about the most similar words of a
    particular word, or finds semantic analogies of some triplets of words. It then prints the results. With this
    function we can estimate the accuracy of our model, and this, we could say that we run some statistical tests for
    it, thus its name model_stats."""

    words_check = ["bible", "book", "bank", "water"]
    for word in words_check:
        print("For the word ", word, " the most similar words that the model produced are:\n", model.wv.most_similar(word))
        print("\n")

    triplets = [("girls", "kings", "queen"), ("good", "taller", "tall"), ("france", "london", "paris")]
    for triplet in triplets:
        print("for the triplet", triplet, "the most similar words were:", model.wv.most_similar(
            positive=[triplet[0], triplet[1]], negative=[triplet[2]]))
        print("\n")
    return


if __name__ == "__main__":

    # read data/gutenberg.txt in the expected format
    read_dir = os.getcwd().rsplit("/", 1)[0] + "/data/preprocessed_sentences.txt"
    with open(read_dir, 'r') as f:
        lines = f.readlines()
    sentences = []
    for line in lines:
        line_words = line.split(" ")
        del line_words[-1]
        sentences.append(line_words)

    
    output_file = os.getcwd().rsplit("/", 1)[0] + "/" + "models/gutenberg_w2v.100d.model"
    window = 9
    embedding_dim = 100
    epochs = 250
    min_word_count = 10

    load_model(output_file)
    # load_pretrained_model()
    """
    train_w2v_model(
        sentences,
        output_file,
        window=window,
        embedding_dim=embedding_dim,
        epochs=epochs,
        min_word_count=min_word_count
    )
    """
