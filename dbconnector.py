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
        self._db = self._connection[kwargs.get('db')]
        self._db.authenticate(kwargs['username'], kwargs['password'])
        self._collection = self._db.get_collection(kwargs.get('table'))

    def _initialize(self, **kwargs):
        pass

    def filter(self, **kwargs):
        items = list()
        cursor = self._collection.find(kwargs, { '_id'  :0 })
        for item in cursor:
            items.append(item)    

        return items
