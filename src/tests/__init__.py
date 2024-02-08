# tests/__init__.py

from .test_cypher import TestCypher
from .test_utile import TestUtile

import os
os.environ['TESTING'] = 'True'
