import nltk.downloader
from nltk.corpus import stopwords
import spacy
from streams import Stream


class NLPProcessor:
    __language = "german"
    __nltk = nltk
    __spacy_nlp = spacy.load('de_core_news_sm')

    __stop_words = None

    def __init__(self):
        self.__nltk.download("punkt")
        self.__nltk.download("stopwords")
        self.__stop_words = set(stopwords.words(self.__language))

    def __stop_word_filter(self, word):
        return word not in self.__stop_words

    def process(self, sentence):
        words_stream = Stream(self.__spacy_nlp(sentence)) \
            .map(lambda r: r.lemma_) \
            .filter(self.__stop_word_filter)
        return list(words_stream)
