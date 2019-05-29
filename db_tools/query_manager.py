import os

path = os.path.dirname(os.path.abspath(__file__))

class QueryManager:

    @staticmethod
    def get_synonyms_query():
        file = open(f'{path}/queries/synonyms.sql', 'r')
        return ''.join(file.readlines())

    @staticmethod
    def get_synsets_query():
        file = open(f'{path}/queries/synsets.sql', 'r')
        return ''.join(file.readlines())
