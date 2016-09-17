"""
Test used only to check if all necessary libs are available
"""
import unittest
import time

from tl_en import tl_en
from hamcrest import *
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

class TestModule(unittest.TestCase):
    def testSum(self):
        assert_that(tl_en.sum(1,3), equal_to(4))

    def testNotifications(self):
        Notify.init("Hello world")
        Hello=Notify.Notification.new("Hello world", "This is an example notification.", "dialog-information")
        Hello.show()
        time.sleep(1)
        Hello.close()
