from abc import ABCMeta, abstractmethod
import pymongo


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
        self._connection = pymongo.MongoClient(host=kwargs.get('host'), port=kwargs.get('port') )
        self._db = self._connection[kwargs.get('db')]
        self._collection = self._db[kwargs.get('table')]

    def _initialize(self, **kwargs):
        pass

    def filter(self, **kwargs):
        return self._collection.find(**kwargs)
