from abc import ABCMeta, abstractmethod
import pymongo
from rfc3986 import urlparse


class DBConnector(metaclass=ABCMeta):
    def __init__(self, **kwargs):
        self._initialize(**kwargs)

    @abstractmethod
    def _initialize(self, **kwargs):
        pass

    @abstractmethod
    def filter(self, **kwargs):
        pass


class MongoConnector(DBConnector):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._connection = pymongo.MongoClient(kwargs.get('uri'))


    def _initialize(self, **kwargs):
        pass

    def filter(self, **kwargs):
        return self._collection.find(**kwargs)
