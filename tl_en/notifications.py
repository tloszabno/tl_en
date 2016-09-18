import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify, GdkPixbuf

import time
import config
from threading import Thread
from Queue import Queue


class NotificationsFasade(object):
    def __init__(self):
        Notify.init("TL-EN")
        self.notifications = Queue()
        self.thread = Thread(target=self.__wait_for_notifications__)
        self.thread.daemon = True
        self.thread.start()

    def __wait_for_notifications__(self):
        while True:
            n = self.notifications.get()
            n()

    def notify(self, word):
        n = lambda: self.__notify_word__(word)
        self.notifications.put(n)

    def __notify_word__(self, word):
        formatted = format_word(word)
        notif = Notify.Notification.new(*formatted)
        image = GdkPixbuf.Pixbuf.new_from_file(config.DICTIONARY_ICON_PATH)
        notif.set_icon_from_pixbuf(image)
        notif.set_image_from_pixbuf(image)

        notif.show()
        time.sleep(config.SHOW_NOTIFICATION_TIME_SEC)
        notif.close()

def format_word(word):
    return '{0: <40}'.format(word[0]), notBlankOrNone("\n".join([word[1], word[2]]))

def notBlankOrNone(w):
    return w if len(w) > 0 else None
