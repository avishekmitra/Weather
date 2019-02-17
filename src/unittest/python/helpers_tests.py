import sys
sys.path.append('/home/amitra/environments/Weather/src/main/python')

import unittest
from datetime import datetime, timedelta
from helpers import getlatlong, getcurrentdate


class MyTest(unittest.TestCase):
     def test_core(self):
       self.assertEqual(getlatlong(33, 44), '33,44')
       self.assertEqual(getcurrentdate(), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
