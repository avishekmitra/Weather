import sys
sys.path.append('/home/amitra/environments/Weather/src/main/python')

import unittest

from subhelpers import getcityname


class MyTest(unittest.TestCase):
     def test_cityname(self):
       self.assertEqual(getcityname('LAS'), 'Las Vegas')
