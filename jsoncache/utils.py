from .errors import CacheUpdateError


def update_dict(source, changes):
    # For compatibility between Python 2 and Python 3
    try:
        whitelisted_types_keys = [str, unicode]
    except:
        whitelisted_types_keys = [str]

    blacklisted_types_values = [set]

    if len(changes) < 2:
        raise CacheUpdateError("Changes {} to be applied are invalid. "
                               "Atleast 2 items should be provided."
                               .format(changes))

    for key in changes[:-1]:
        if type(key) not in whitelisted_types_keys:
            raise CacheUpdateError("Changes {} to be applied are invalid. "
                                   "Keys to be updated should be {}"
                                   .format(changes, whitelisted_types_keys))

    for key in changes[:-2]:
        if key not in source:
            source[key] = {}
        elif type(source[key]) != dict:
            raise CacheUpdateError("Changes {} to be applied are invalid. "
                                   .format(changes))
        source = source[key]

    if type(changes[-1]) in blacklisted_types_values:
        raise CacheUpdateError("Changes {} to be applied are invalid. "
                               "Value to be stored should not be {}"
                               .format(changes, blacklisted_types_values))

    source[changes[-2]] = changes[-1]
