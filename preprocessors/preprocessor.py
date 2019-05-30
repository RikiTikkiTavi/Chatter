from streams import Stream
from preprocessors.nlp_processor import NLPProcessor
from preprocessors.syn_processor import SynProcessor


class Preprocessor:
    __nlp_proc = None
    __syn_proc = None

    def __init__(self, database_service):
        self.__nlp_proc = NLPProcessor()
        self.__syn_proc = SynProcessor(database_service)

    def process_single(self, sentence_raw):
        words_processed = self.__nlp_proc.process(sentence_raw)
        return self.__syn_proc.process(words_processed, sentence_raw)

    def process_multiple(self, sentence_raw_list):
        return list(map(self.process_single, sentence_raw_list))
