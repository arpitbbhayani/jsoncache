import json

from .errors import CacheIOError


def write_json(filepath, d):
    try:
        with open(filepath, 'w') as f:
            json.dump(d, f, sort_keys=True, indent=4)
    except IOError as e:
        raise CacheIOError("Error while reading from cache: {}"
                           .format(str(e)))


def read_json(filepath):
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except IOError as e:
        raise CacheIOError("Error while reading from cache: {}"
                           .format(str(e)))
    except ValueError as e:
        raise CacheIOError("Invalid cache file")
