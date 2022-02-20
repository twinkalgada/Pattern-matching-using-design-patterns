from AbstractHandler import AbstractHandler

class StarHandler(AbstractHandler):
    # Star handler will see if the '*' from pattern matches any 0 or more position until the next character in the
    # pattern i.e. t
    def __init__(self, pattern_index, pattern):
        self._pattern_index = pattern_index
        self._pattern = pattern

    def handle(self, position, target_string) -> str:
        orig_position = position
        for _ in target_string[position::]:
            if self._pattern_index + 1 < len(self._pattern):
                res = super().handle(position, target_string)
                if res == -1:
                    position += 1
            return orig_position