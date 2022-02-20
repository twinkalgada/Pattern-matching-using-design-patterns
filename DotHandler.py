from AbstractHandler import AbstractHandler

class DotHandler(AbstractHandler):
    # Dot handler will see if the '.' from pattern matches any 1 position at the position given in target string
    def __init__(self, pattern_index, pattern):
        self._pattern_index = pattern_index
        self._pattern = pattern

    def handle(self, position, target_string) -> int:
        if position + 1 < len(target_string) and self._pattern_index + 1 < len(self._pattern):
            res = super().handle(position + 1, target_string)
            if res == -1:
                return -1
            else:
                return position