# jsoncache

**jsoncache** is a file-based cache though which you can put and fetch
data; thus giving you an ability to easily update a small chunk of data in
a JSON file. In short you can use this library to manipulate any JSON file.

## Motivation
For storing data in [bucket-list](https://github.com/arpitbbhayani/bucket-list)
for any external provider like Wunderlist, I used to make a lot of network
calls. Some of those calls were redundant. Because of these redundant calls
the utility became slower when any external provider is used. So I created
**jsoncache** which can help me cache the responses of some of the API calls
and eventually make the utility faster.

## Installation
Installing `jsoncache` is as easy as

```bash
pip install jsoncache
```

## Getting started with jsoncache

```python
>>> from jsoncache import JSONCache
>>> j = JSONCache('cache.json')
>>> j.put('name', 'firstname', 'Arpit')
>>> j.get('name', 'firstname')
'Arpit'
```

To initialize a JSONCache you should pass filepath as the argument. This will
return you an instance of `JSONCache`. This file is where all your cache
content will be stored.

`.put(*args)` and `.get(*args)` are two methods exposed in JSONCache object
which are used to put something into cache and get something from the cache.
The last argument passed in `put` method should be the value (object) to be
stored in cache and this object should be JSON serializable.

If something is not cache and you are trying to fetch it,
`NotInCacheError` error is raised.

More info about `get`, `put`, `delete` and `errors` can be found in
documentation [here](../../wiki).

## Documentation
A compehensive documentation can be found [here](../../wiki).
Lot of efforts have been put into this, hope you find it useful :smile:

## Contribution
In case you loved this utility and have a great feature idea, then feel free
to contribute . The complete utility is written in
[Python](https://docs.python.org/). So for contributing all you need to have
is working knowledge of Python.

You can find source code [here](https://github.com/arpitbbhayani/jsoncache).

Here are some [ideas](../../wiki/Future-Features) that you may love to work on.

## Issues
Please report any glitch, bug, error or an unhandled exception :frowning: Feel
free to [create one](../../issues/new).
