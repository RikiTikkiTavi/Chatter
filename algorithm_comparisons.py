from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
import nltk.downloader
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')

language = 'german'
question = "Hast du eine neue Nachricht gehört?"
question_base = "Hast du die Nachrichten gehört?"


def pre_process(text):
    stop_words = set(stopwords.words(language))

    words = word_tokenize(text, language)

    stemmer = SnowballStemmer(language)

    return ' '.join(
        list(
            map(stemmer.stem,
                filter(
                    lambda w: w not in stop_words,
                    words
                ))
        )
    )


question_processed = pre_process(question)
question_base_processed = pre_process(question_base)

tfidf = TfidfVectorizer()

corpus = [question_processed, question_base_processed]

X = tfidf.fit_transform(corpus)

cosine_similarities_matrix = (X * X.T).A

print("Sentences similarity with preprocessing: ", cosine_similarities_matrix[0][1])
