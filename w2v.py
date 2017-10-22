# -*- coding: utf-8 -*-

from gensim.models import word2vec
import logging

def main():
    filePath = "C:\\Users\\Java\\Desktop\\TM"
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.Text8Corpus(filePath + '\\word2Vec\\KyotoW2V\\segedv3.txt')
    model = word2vec.Word2Vec(sentences, size=250)

    # Save our model.
    model.save("med250.model.bin")

    # To load a model.
    # model = word2vec.Word2Vec.load("your_model.bin")

if __name__ == "__main__":
    main()