import schedule
import config


class SendingDaemon(object):
    def __init__(self, wordsDB):
        self.wordsDB = wordsDB
        self.listeners = []

    def register_listener(self, listener):
        self.listeners.append(listener)

    def run(self):
        schedule.every(config.SENDING_INTERVAL_MIN).minutes.do(self.job)

    def job(self):
        word = self.wordsDB.get_random_word()
        if word:
            map(lambda listener: listener(word), self.listeners)
