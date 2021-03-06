
class TypeProfile:

    # import_statements = [
    # ]

    supports_type_lookup = """
        return False"""

    supports_type_admin = """
        return False"""


class TypeManager:

    import_statements = [
        'from ..osid.osid_errors import Unimplemented',
    ]

    get_type_lookup_session = """
        raise Unimplemented()"""

    get_type_admin_session = """
        raise Unimplemented()"""


class TypeProxyManager:

    import_statements = [
        'from ..osid.osid_errors import Unimplemented',
    ]

    get_type_lookup_session = """
        raise Unimplemented()"""

    get_type_admin_session = """
        raise Unimplemented()"""


class TypeList:

    import_statements = [
        'from ..osid.osid_errors import IllegalState, OperationFailed',
        'from ..osid.objects import OsidList',
        'from ..primitives import Type',
    ]

    get_next_type = """
        try:
            next_item = next(self)
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        except:  # Need to specify exceptions here
            raise OperationFailed()
        else:
            return next_item

    def next(self):
        try:
            next_item = OsidList.next(self)
        except:
            raise
        if isinstance(next_item, dict):
            next_item = Type(next_item)
        return next_item

    __next__ = next
    next_type = property(fget=get_next_type)"""

    get_next_types = """
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            i = 0
            while i < n:
                try:
                    next_list.append(next(self))
                except:  # Need to specify exceptions here
                    raise OperationFailed()
                i += 1
            return next_list"""
