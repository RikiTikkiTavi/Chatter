class Executor:
    result_handler = None
    cursor = None

    def __init__(self, result_handler, cursor):
        self.result_handler = result_handler
        self.cursor = cursor

    def do_query(self, query):
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        return self.result_handler.handle(records)
