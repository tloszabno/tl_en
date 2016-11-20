import unittest
from hamcrest import *
from mockito import *
from tl_en import WordsDB
from tl_en import WordsService
from tl_en import notifications
from tl_en import config


class DBDummy(object):
    def get_next_random_part(self, size):
        return [("word_%d" % i, "def_%d" % i) for i in xrange(size)]


class TestBasic(unittest.TestCase):
    def setUp(self):
        self.db = DBDummy()
        self.words_service = WordsService.WordsService(self.db)

    def test_should_return_nofication_obj(self):
        got = self.words_service.get()
        assert_that(got, instance_of(notifications.Notification))
