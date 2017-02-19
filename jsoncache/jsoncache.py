import os

from . import fileio
from . import utils
from .errors import (CacheError, ArgumentError, CacheIOError,
                     NotInCacheError)


class JSONCache:
    def __init__(self, cache_filepath):
        self.fp = cache_filepath

        if os.path.isdir(self.fp):
            raise CacheIOError("Error while initializing cache: {}"
                               .format("Folder exists instead of file"))

        if not os.path.exists(self.fp):
            fileio.write_json(self.fp, {})
        fileio.read_json(self.fp)

    def get(self, *args):
        if len(args) == 0:
            raise ArgumentError("Atleast one key should be given.")

        data = fileio.read_json(self.fp)
        try:
            for k in args:
                data = data[k]
        except KeyError as e:
            raise NotInCacheError("Path {} does not exist in cache"
                                  .format(args))
        return data

    def put(self, *args):
        if len(args) == 0:
            raise ArgumentError("Atleast key and value should be given")

        if len(args) == 1:
            raise ArgumentError("Value to be stored not given")

        data = fileio.read_json(self.fp)
        utils.update_dict(data, args)
        fileio.write_json(self.fp, data)

    def delete(self, *args):
        if len(args) == 0:
            raise ArgumentError("Atleast one key should be given.")

        cache_data = data = fileio.read_json(self.fp)
        try:
            for k in args[:-1]:
                data = data[k]
            if type(data) is not dict:
                raise NotInCacheError("Path {} does not exist in cache"
                                      .format(args))
            del data[args[-1]]
        except KeyError as e:
            raise NotInCacheError("Path {} does not exist in cache"
                                  .format(args))
        fileio.write_json(self.fp, cache_data)
