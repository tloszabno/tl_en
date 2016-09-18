#!/usr/bin/env python

from SendingDaemon import SendingDaemon
from WordsDB import WordsDB
import config
import schedule
import time
import notifications

def run_daemon():
    notifs = notifications.NotificationsFasade()
    db = WordsDB(config.WORDS_DICTIONARY_PATH)

    daemon = SendingDaemon(db)
    daemon.register_listener(notifs.notify)
    daemon.run()

    while True:
        schedule.run_pending()
        time.sleep(1)

def main():
    #TODO client, options etc
    run_daemon()

if __name__ == '__main__':
    main()
