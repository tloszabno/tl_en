import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

import time
import config
from threading import Thread


class NotificationsFasade(object):
    def __init__(self):
        Notify.init("TL-EN")

    def notify(self, word):
        t = Thread(target=self.__notify_word__, args=(word,))
        t.daemon = True
        t.start()

    def __notify_word__(self, word):
        print "notify " + str(word)
        n = Notify.Notification.new(
            word[0],
            notBlankOrNone("\n".join([word[1], word[2]])),
            "dialog-information" # dialog-warn, dialog-error
        )
        n.show()

        time.sleep(config.SHOW_NOTIFICATION_TIME_SEC)

        n.close()

def notBlankOrNone(w):
    return w if len(w) > 0 else None
