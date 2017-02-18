class CacheError(Exception):
    def __init__(self, description, error_code=None):
        Exception.__init__(self)
        self.description = description
        self.error_code = error_code

    def __str__(self):
        return "{}".format(self.description)


class NotInCacheError(CacheError):
    def __init__(self, description):
        CacheError.__init__(self, description, error_code='NOT_IN_CACHE')


class CacheIOError(CacheError):
    def __init__(self, description):
        CacheError.__init__(self, description, error_code='CACHE_IO_ERROR')


class CacheInitError(CacheError):
    def __init__(self, description):
        CacheError.__init__(self, description, error_code='CACHE_INIT_ERROR')


class ArgumentError(CacheError):
    def __init__(self, description):
        CacheError.__init__(self, description, error_code='ARGUMENT_ERROR')


class CacheUpdateError(CacheError):
    def __init__(self, description):
        CacheError.__init__(self, description, error_code='CACHE_UPDATE_ERROR')
