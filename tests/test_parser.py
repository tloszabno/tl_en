# -*- coding: utf-8 -*-

import unittest
from hamcrest import *
from tl_en import parser
import config
import os
import logging

class TestParser(unittest.TestCase):
    def test_should_parse_valid_file_with_one_line(self):
        # given
        input_file = config.TEST_DATA_PATH + os.sep + "input_one_row_valid.txt"
        # when
        result = parser.parse_file(input_file)
        #then
        assert_that(result, has_length(1))
        assert_that(result[0][0], equal_to_ignoring_case("house"))
        assert_that(result[0][1], equal_to_ignoring_case("dom"))
        assert_that(result[0][2], equal_to_ignoring_case("be in the house"))

    def test_should_parse_valid_file_with_tree_line(self):
        # given
        input_file = config.TEST_DATA_PATH + os.sep + "input_tree_row_valid.txt"
        # when
        result = parser.parse_file(input_file)
        #then
        assert_that(result, has_length(3))

        assert_that(result[0][0], equal_to_ignoring_case("house"))
        assert_that(result[0][1], equal_to_ignoring_case("dom"))
        assert_that(result[0][2], equal_to_ignoring_case("be in the house"))

        assert_that(result[1][0], equal_to_ignoring_case("chair"))
        assert_that(result[1][1], equal_to_ignoring_case("krzesło"))
        assert_that(result[1][2], equal_to_ignoring_case("the chair is in the room\nkrzesło jest w pokoju"))

        assert_that(result[2][0], equal_to_ignoring_case("light"))
        assert_that(result[2][1], equal_to_ignoring_case("światło"))

    def test_should_parse_file_with_empty_places(self):
        # given
        input_file = config.TEST_DATA_PATH + os.sep + "file_with_empty_places.txt"
        # when
        result = parser.parse_file(input_file)
        #then
        assert_that(result, has_length(2))

        assert_that(result[0][0], equal_to_ignoring_case("house"))
        assert_that(result[0][1], equal_to_ignoring_case("dom"))
        assert_that(result[0][2], equal_to_ignoring_case("be in the house"))

        assert_that(result[1][0], equal_to_ignoring_case("light"))
        assert_that(result[1][1], empty())
        assert_that(result[1][2], empty())
