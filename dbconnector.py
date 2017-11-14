from abc import ABCMeta, abstractmethod
import pymongo


class DBConnector(metaclass=ABCMeta):
    @abstractmethod
    def _initialize(self, *args):
        pass

    @abstractmethod
    def filter(self, **kwargs):
        pass


class MongoConnector(DBConnector):
    def __init__(self, *args):
        self.connection = pymongo.MongoClient()
        self._initialize(args)

    def _initialize(self, *args):
        pass

    def filter(self, **kwargs):
        pass
