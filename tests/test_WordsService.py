import unittest

from hamcrest import *

from tl_en.WordsService import WordsService
from tl_en import notifications


class DBDummy(object):
    def get_next_random_part(self, size):
        return [("word_%d" % i, "def_%d" % i) for i in range(size)]


class TestBasic(unittest.TestCase):
    def setUp(self):
        self.db = DBDummy()
        self.words_service = WordsService(self.db)

    def test_should_return_nofication_obj(self):
        got = self.words_service.get()
        assert_that(got, instance_of(notifications.Notification))
