from resources.questions import questions
import json
from preprocessors.preprocessor import Preprocessor
from db_tools.db_service import DBService

dbs = DBService()
preprocessor = Preprocessor(dbs)

questions_processed = preprocessor.process_multiple(questions)

print(questions_processed)

q_file = open('questions_processed.json', 'w+')

json_questions = json.dumps(questions_processed)

q_file.write(json_questions)
