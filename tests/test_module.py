"""
Test used only to check if all necessary libs are available
"""
import unittest

from tl_en import tl_en
from hamcrest import *

class TestModule(unittest.TestCase):
    def TestSum(self):
        assert_that(tl_en.sum(1,3), equal_to(4))
        print("Module structure ok, libs imported")
