import abc


class ResultHandler:

    @staticmethod
    @abc.abstractmethod
    def do_handle(records):
        return list(map(lambda r: r[0], records))

    @staticmethod
    def handle(records):
        handled = __class__.do_handle(records)
        return handled
