#!/usr/bin/env python

from SendingDaemon import SendingDaemon
from WordsDB import WordsDB
import config
import schedule
import time


def listener(w):
    print w

def run_daemon():
    db = WordsDB(config.WORDS_DICTIONARY_PATH)
    daemon = SendingDaemon(db)
    daemon.register_listener(listener)
    daemon.run()
    while True:
        schedule.run_pending()
        time.sleep(10)

def main():
    #TODO client, options etc
    run_daemon()

if __name__ == '__main__':
    main()
