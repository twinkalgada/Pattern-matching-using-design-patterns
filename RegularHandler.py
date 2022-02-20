from AbstractHandler import AbstractHandler

class RegularHandler(AbstractHandler):
    # RegularHandler will see if the character from pattern matches with the character at the position given in
    # target string
    def __init__(self, pattern_index, pattern):
        self._pattern_index = pattern_index
        self._pattern = pattern

    def handle(self, position, target_string) -> int:
        if target_string[position] == self._pattern[self._pattern_index]:
            if position + 1 < len(target_string) and self._pattern_index + 1 < len(self._pattern):
                res = super().handle(position + 1, target_string)
                if res == -1:
                    return -1
            return position
        else:
            return -1