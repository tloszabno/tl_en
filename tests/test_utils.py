import unittest
from hamcrest import *
from tlen import utils


class Test_head_and_tail_each_new_line(unittest.TestCase):

    def test_should_return_double_tuple_from_4_elements(self):
        # given
        _tuple = ('1', '2', '3', '4')

        # when
        got = utils.head_and_tail_each_new_line(_tuple)

        # then
        expected = ('1', '2\n3\n4')
        assert_that(got, equal_to(expected))

    def test_should_return_double_tuple_with_second_none(self):
        # given
        _tuple = ('1')

        # when
        got = utils.head_and_tail_each_new_line(_tuple)

        # then
        expected = ('1', None)
        assert_that(got, equal_to(expected))
