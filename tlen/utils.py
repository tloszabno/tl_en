def head_and_tail_each_new_line(tuple):
    tail = not_blank_or_none("\n".join(tuple[1:]))
    return not_blank_or_none(tuple[0]), not_blank_or_none(tail)


def not_blank_or_none(w):
    return w if w and len(w) > 0 else None
