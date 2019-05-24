import os


class QueryManager:
    @staticmethod
    def get_synonyms_query():
        file = open('./queries/synonyms.sql', 'r')
        return ''.join(file.readlines())

