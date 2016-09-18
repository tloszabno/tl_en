import random
import parser
import schedule
import config

class WordsDB(object):
    def __init__(self, file_name):
            self.file_name = file_name
            self.words = []
            self.refresh_cache()
            schedule.every(config.WORDS_CACHE_REFRESH_INTERVAL_H).hours.do(self.refresh_cache)

    def refresh_cache(self):
        self.words = parser.parse_file(self.file_name)
        print "Cache refreshed, got: " + str(self.words)

    def get_random_word(self):
        return random.choice(self.words)
