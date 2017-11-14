from abc import ABCMeta, abstractmethod
import pymongo


class DBConnector(metaclass=ABCMeta):
    @abstractmethod
    def filter(self, **kwargs):
        pass

    @abstractmethod
    def insert(self, **kwargs):
        pass


class MongoConnector(DBConnector):
    def __init__(self, **kwargs):
        self._connection = pymongo.MongoClient(kwargs.get('uri'))
        self._db = self._connection[kwargs.get('db')]
        self._db.authenticate(kwargs['username'], kwargs['password'])
        self._collection = self._db.get_collection(kwargs.get('table'))

    def filter(self, kwargs):
        items = list()
        if kwargs:
            cursor = self._collection.find(kwargs)
        else:
            cursor = self._collection.find()
        for item in cursor:
            item.pop("_id")
            items.append(item)

        return items

    def insert(self, kwargs):
        _, values = kwargs.popitem()
        self._collection.insert_many(values)
