from tl_en import config
from tl_en.notifications import Notification
from threading import Lock
import random


class WordsService(object):
    def __init__(self, words_db):
        self.words_db = words_db
        self.words_to_notify = []
        self.lock = Lock()
        self.last_result = ""
        self.update_word_to_notify()

    def get(self):
        """method for notify sending job"""
        with self.lock:
            return self.__get_random_word__()

    def __get_random_word__(self):
        if len(self.words_to_notify) == 0:
            return None
        while True:
            result = random.choice(self.words_to_notify)
            if result != self.last_result:
                self.last_result = result
                return result

    def update_word_to_notify(self):
        with self.lock:
            self.words_to_notify = []
            part = (self.words_db
                    .get_next_random_part(config.NUMBER_OF_WORDS_IN_GROUP))
            self.words_to_notify = [Notification(n) for n in part]
            print("Group updated to: " + str(part))
