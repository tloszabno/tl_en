import time
from tl_en import config
from threading import Thread
from multiprocessing import Queue
import gi
from tl_en import utils

gi.require_version('Notify', '0.7')


class Notification(object):
    def __init__(self, word_tuple):
        if not word_tuple:
            (self.header, self.description) = ("", "")
            return
        (self.header, self.description) = utils.head_and_tail_each_new_line(word_tuple)

    def to_formatted_tuple(self):
        return '{0: <30}'.format(self.header), self.description


class NotificationsFasade(object):
    def __init__(self):
        from gi.repository import Notify
        Notify.init(config.MODULE_NAME)
        self.notifications = Queue()
        self.thread = Thread(target=self.__wait_for_notifications__)
        self.thread.daemon = True
        self.thread.start()

    def __wait_for_notifications__(self):
        while True:
            notification = self.notifications.get()
            notification()

    def notify(self, word):
        self.notifications.put(lambda: self.__notify_word__(word))

    def __notify_word__(self, notification):
        from gi.repository import Notify, GdkPixbuf
        notif = Notify.Notification.new(*notification.to_formatted_tuple())
        image = GdkPixbuf.Pixbuf.new_from_file(config.NOTIFICATION_ICON_PATH)
        notif.set_icon_from_pixbuf(image)
        notif.set_image_from_pixbuf(image)

        notif.show()
        time.sleep(config.SHOW_NOTIFICATION_TIME_SEC)
        notif.close()
