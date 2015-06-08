"""mongo utilities.py"""
from .osid.osid_errors import NullArgument, NotFound, OperationFailed

from . import mongo_client


class MongoClientValidated(object):
    """automatically validates the insert_one, find_one, and delete_one methods"""
    def __init__(self, db, collection):
        self._mc = mongo_client[db][collection]

    def _validate_write(self, result):
        try:
            if not result.acknowledged or result.inserted_id is None:
            # if (('writeErrors' in result and len(result['writeErrors']) > 0) or
            #         ('writeConcernErrors' in result and len(result['writeConcernErrors']) > 0)):
                raise OperationFailed(str(result))
        except AttributeError:
            # account for deprecated save() method
            if result is None:
                raise OperationFailed('Nothing saved to database.')

    def count(self):
        return self._mc.count()

    def delete_one(self, query):
        result = self._mc.delete_one(query)
        if result is None or result.deleted_count == 0:
            raise NotFound(str(query) + ' returned None.')
        return result

    def find(self, query=None):
        if query is None:
            return self._mc.find()
        else:
            return self._mc.find(query)

    def find_one(self, query):
        result = self._mc.find_one(query)
        if result is None:
            raise NotFound(str(query) + ' returned None.')
        return result

    def insert_one(self, doc):
        result = self._mc.insert_one(doc)
        self._validate_write(result)
        return result

    def save(self, doc):
        result = self._mc.save(doc)
        self._validate_write(result)
        return result

def arguments_not_none(func):
    """decorator, to check if any arguments are None; raise exception if so"""
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg is None:
                raise NullArgument()
        for arg, val in kwargs.iteritems():
            if val is None:
                raise NullArgument()
        try:
            return func(*args, **kwargs)
        except TypeError as ex:
            if 'takes exactly' in ex.args[0]:
                raise NullArgument('Not all arguments provided: ' + str(ex.args[0]))
            else:
                raise TypeError(*ex.args)

    return wrapper