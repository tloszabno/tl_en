import random
import parser
import schedule
import config

class WordsDB(object):
    def __init__(self, file_name):
            self.file_name = file_name
            self.words = []
            self.refresh_cache()
            self.last_result = ""
            schedule.every(config.WORDS_CACHE_REFRESH_INTERVAL_H).hours.do(self.refresh_cache)

    def refresh_cache(self):
        self.words = parser.parse_file(self.file_name)
        print "Cache refreshed, got: " + str(self.words)

    def get_random_word(self):
        if len(self.words) == 0:
            return None
        while True:
            result = random.choice(self.words)
            if result != self.last_result:
                self.last_result = result
                return result
