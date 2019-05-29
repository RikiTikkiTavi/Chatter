from db_tools.db_service import DBService
from preprocessors.preprocessor import Preprocessor
from resources.questions import questions
import json
from streams import Stream

dbs = DBService()
pre = Preprocessor()

processed_words_arrs = list(map(pre.process, questions))

sentences = []

for s_i, s in enumerate(processed_words_arrs):
    sentence = {
        'sentence': ' '.join(s),
        'words': []
    }
    for w_i, w in enumerate(s):
        sentence['words'].append({
            'word': w,
            'synsets': dbs.get_synsets(w)
        })
    sentences.append(sentence)

q_file = open('questions_processed.json', 'w+')

json_questions = json.dumps(sentences)

q_file.write(json_questions)
