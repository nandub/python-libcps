from dbcps.sinks.core import Sink
import os

# Module is renamed in Python 3
try:
    import anydbm
except:
    import dbm as anydbm

class ADBM(Sink):
    '''
    Uses the anydbm module to store data to disc.

    >>> from dbcps import storage
    >>> from tempfile import mkstemp
    >>> tempfile = mkstemp()
    >>> fname = tempfile[1]
    >>> backend = ('adbm', fname, ['rotate', -91])
    >>> del tempfile
    >>> s = storage.Storage([backend])
    >>> s['hello'] = 'world'
    >>> s['hello']
    'world'
    >>> 'hello' in s
    True
    >>> 'hell' in s
    False
    >>> del s['hello']
    >>> 'hello' in s
    False
    >>> s['blueberry'] = 'pancakes'
    >>> del s
    >>> s = storage.Storage([backend])
    >>> s['blueberry']
    'pancakes'
    '''

    def __init__(self, path, origin = None, filemode='c'):
        Sink.__init__(self, origin)
        filesize = os.stat(path).st_size
        if filesize == 0:
            os.remove(path)
        self.backend = anydbm.open(path, filemode)
