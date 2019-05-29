from db_tools.db_service import DBService


class SynProcessor:
    def __init(self):
        self.dbs = DBService()

    def process(self, words):
        sentence = {
            'sentence': ' '.join(words),
            'words': []
        }
        for w in words:
            sentence['words'].append({
                'word': w,
                'synsets': self.dbs.get_synsets(w)
            })
        return sentence
