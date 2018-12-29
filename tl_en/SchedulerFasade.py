import schedule
from tl_en import config


def tick():
    schedule.run_pending()


def schedule_sending_notifications(runnable):
    schedule.every(config.SENDING_INTERVAL_MIN).minutes.do(runnable)


def schedule_cache_refresh(runnable):
    schedule.every(config.WORDS_CACHE_REFRESH_INTERVAL_H).hours.do(runnable)


def schedule_words_groups_refresh(runnable):
    (schedule
        .every(config.INTERVAL_TO_REFRESH_GROUP_WORDS_MIN)
        .minutes
        .do(runnable))
