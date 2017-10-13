"""walk the directory to find all source files"""

import os
import glob
from collections import Iterable

class SourceWalker(Iterable):
    
    def __init__(self, full_pattern):
        self.pattern = full_pattern
    
    def __iter__(self):
        pat = glob.iglob(self.pattern)
        for fp in pat:
            yield fp

def join(dirname, pattern):
    return SourceWalker(os.path.join(dirname, pattern))

class Walker(object):
    """walks and loads file types"""
    _patterns = ["*.md", "*.jinja2", "*.html"]

    def __init__(self, outpath):
        self.outpath = outpath
        self.walkers = map(lambda x: join(self.outpath, x), self._patterns)

    def __iter__(self):
        for walker in self.walkers:
            for fp in walker:
                yield fp