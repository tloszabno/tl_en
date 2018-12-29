import random
import parser


class WordsDB(object):
    def __init__(self, file_name):
            self.file_name = file_name
            self.words = []
            self.refresh_cache()

    def refresh_cache(self):
        self.words = parser.parse_file(self.file_name)
        print("Cache refreshed, got: " + str(self.words))

    def get_next_random_part(self, size):
        if size > len(self.words):
            return self.words[:]  # copy

        start_idx = random.randint(0, len(self.words))
        end_inx = start_idx + size
        if end_inx < len(self.words):
            return self.words[start_idx:end_inx + 1]
        part = self.words[start_idx:]
        return part + self.words[0:size-len(part)+1]
