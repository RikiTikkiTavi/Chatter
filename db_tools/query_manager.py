import os


class QueryManager:
    @staticmethod
    def get_synonyms_query():
        file = open('./synonyms.sql', 'r')
        return '\n'.join(file.readlines())

