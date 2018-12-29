__SEPARATOR__ = "-"


def parse_file(file_path):
    result = []
    with open(file_path) as fs:
        for entry in fs:
            chunks = entry.split(__SEPARATOR__)
            if len(chunks) == 0:
                continue

            english_word = chunks[0].strip()
            if len(english_word) == 0:
                continue
            translation = chunks[1].strip() if len(chunks) > 1 else ""
            sample = "\n".join([x.strip() for x in chunks[2:]])
            result.append((english_word, translation, sample))
    return result
