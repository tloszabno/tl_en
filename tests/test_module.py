"""
Test used only to check if all necessary libs are available
"""
import unittest
import time
from tl_en import tl_en
from tl_en import parser
from hamcrest import *
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify, GdkPixbuf


class TestModule(unittest.TestCase):
    def testNotifications(self):
        Notify.init("Test notification")
        Hello= Notify.Notification.new("Test notification", "Test ok", "dialog-information")
        Hello.show()
        time.sleep(0.2)
        Hello.close()
