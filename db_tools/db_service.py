import mysql.connector
from .config import user
from .config import password
from .config import db_name
from .executor import Executor
from .result_handlers.synonyms_result_handler import SynonymsResultHandler
from .result_handlers.synsets_result_handler import SynsetsResultHandler
from .query_manager import QueryManager


class DBService:
    connection = None
    cursor = None

    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user=user,
            passwd=password,
            database=db_name
        )
        self.cursor = self.connection.cursor()

    def get_synonyms(self, word):
        ex = Executor(SynonymsResultHandler, self.cursor)
        query = QueryManager.get_synonyms_query().format(word)
        return ex.do_query(query)

    def get_synsets(self, word):
        ex = Executor(SynsetsResultHandler, self.cursor)
        query = QueryManager.get_synsets_query().format(word)
        return ex.do_query(query)
