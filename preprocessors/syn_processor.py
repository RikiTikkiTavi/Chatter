class SynProcessor:
    dbs = None

    def __init__(self, database_service):
        self.dbs = database_service

    def process(self, words_processed, sentence_raw):
        sentence = {
            'sentence_raw': sentence_raw,
            'words': []
        }
        for w in words_processed:
            sentence['words'].append({
                'word': w,
                'synsets': self.dbs.get_synsets(w)
            })
        return sentence
