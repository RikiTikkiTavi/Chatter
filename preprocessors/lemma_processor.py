class LemmaProcessor:
    __spacy_nlp = None

    def __init__(self, lang_model):
        self.__spacy_lang_model = lang_model

    def get_lemmas(self, text):
        doc = self.__spacy_nlp(text)
        return map(lambda r: r.lemma, doc)

    def get_lemma(self, word):
        doc = self.__spacy_nlp(word)
        return doc[0].lemma
