"""Creating fragments takes a long time so we treat it as a
pre-processing step."""
import logging

from gensim.models import Word2Vec
from cat.fragments import create_noun_counts
from cat.utils import conll2text

logging.basicConfig(level=logging.INFO)


if __name__ == "__main__":

    paths = ["../data/my_data/Restaurants_Train_v2_Semeval2014.conllu"]
    create_noun_counts(paths,
                       "../data/nouns_restaurant.json")
    conll2text(paths, "../data/all_txt_restaurant.txt")
    corpus = [x.lower().strip().split()
              for x in open("../data/all_txt_restaurant.txt")]

    f = Word2Vec(corpus,
                 sg=0,
                 negative=5,
                 window=10,
                 size=200,
                 min_count=2,
                 iter=5,
                 workers=10)

    f.wv.save_word2vec_format(f"../embeddings/my_word_vectors.vec")
