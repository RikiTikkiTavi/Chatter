from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
import nltk.downloader
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import spacy
from spacy.lemmatizer import Lemmatizer
from .lemma_processor import LemmaProcessor
from streams import Stream


# Must be instantiated once
# TODO: Implement singleton
class Preprocessor:
    __language = "german"
    __nltk = nltk
    __spacy_nlp = spacy.load('de_core_news_sm')

    __stop_words = None

    def __init__(self):
        self.__nltk.download("punkt")
        self.__nltk.download("stopwords")
        self.__stop_words = set(stopwords.words(self.__language))

    def process(self, text):
        words_stream = Stream(self.__spacy_nlp(text)) \
            .filter(lambda r: r.is_stop is not True) \
            .map(lambda r: r.lemma_)
        return list(words_stream)
