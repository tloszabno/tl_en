import time
import config
from threading import Thread
from Queue import Queue
import gi
gi.require_version('Notify', '0.7')


class NotificationsFasade(object):
    def __init__(self):
        from gi.repository import Notify
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
        self.notifications.put(lambda: self.__notify_word__(word))

    def __notify_word__(self, word):
        from gi.repository import Notify, GdkPixbuf
        formatted = format_word(word)
        notif = Notify.Notification.new(*formatted)
        image = GdkPixbuf.Pixbuf.new_from_file(config.DICTIONARY_ICON_PATH)
        notif.set_icon_from_pixbuf(image)
        notif.set_image_from_pixbuf(image)

        notif.show()
        time.sleep(config.SHOW_NOTIFICATION_TIME_SEC)
        notif.close()


def format_word(word):
    definition = notBlankOrNone("\n".join([word[1], word[2]]))
    return '{0: <40}'.format(word[0]), definition


def notBlankOrNone(w):
    return w if len(w) > 0 else None
