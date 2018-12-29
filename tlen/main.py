#!/usr/bin/env python3

from Sender import Sender
from WordsDB import WordsDB
from WordsService import WordsService
import SchedulerFasade as scheduler
import config
import notifications
import time


def run_daemon():
    notifs = notifications.NotificationsFasade()
    db = WordsDB(config.WORDS_DICTIONARY_PATH)
    words_service = WordsService(db)
    daemon = Sender(words_service)
    daemon.register_listener(notifs.notify)

    scheduler.schedule_sending_notifications(daemon.send)
    scheduler.schedule_cache_refresh(db.refresh_cache)
    (scheduler
     .schedule_words_groups_refresh(words_service.update_word_to_notify))

    while True:
        # TODO: async socket read for commands from client gui
        scheduler.tick()
        time.sleep(config.MAIN_LOOP_SLEEP_TIME_SEC)


def main():
    # TODO client, options etc
    run_daemon()


if __name__ == '__main__':
    main()
