#!/usr/bin/env python

from SendingDaemon import SendingDaemon
from WordsDB import WordsDB
from WordsService import WordsService
import config
import schedule
import time
import notifications


def run_daemon():
    notifs = notifications.NotificationsFasade()
    db = WordsDB(config.WORDS_DICTIONARY_PATH)
    words_service = WordsService(db)
    daemon = SendingDaemon(words_service)
    daemon.register_listener(notifs.notify)
    daemon.run()

    while True:
        schedule.run_pending()
        time.sleep(config.DAEMON_MAIN_LOOP_SLEEP_TIME_SEC)


def main():
    # TODO client, options etc
    run_daemon()


if __name__ == '__main__':
    main()
