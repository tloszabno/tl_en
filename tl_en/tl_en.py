#!/usr/bin/env python

from Sender import Sender
from WordsDB import WordsDB
from WordsService import WordsService
import config
import time
import notifications
import SchedulerFasade as tl_scheduler


def run_daemon():
    notifs = notifications.NotificationsFasade()
    db = WordsDB(config.WORDS_DICTIONARY_PATH)
    words_service = WordsService(db)
    daemon = Sender(words_service)
    daemon.register_listener(notifs.notify)

    tl_scheduler.schedule_sending_notifications(daemon.send)
    tl_scheduler.schedule_cache_refresh(db.refresh_cache)
    (tl_scheduler
        .schedule_words_groups_refresh(words_service.update_word_to_notify))

    while True:
        # TODO: async socket read for commands from client gui
        tl_scheduler.tick()
        time.sleep(config.MAIN_LOOP_SLEEP_TIME_SEC)


def main():
    # TODO client, options etc
    run_daemon()


if __name__ == '__main__':
    main()
