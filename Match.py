from RegularHandler import RegularHandler
from DotHandler import DotHandler
from StarHandler import StarHandler

class Match():
    def __init__(self, pattern):
        self._pattern = pattern

    # Return the first occurrence of the pattern matching the target string
    def find_first_in(self, target_string):
        if len(self._pattern) > 0 and len(target_string) > 0:
            # Create chain of objects depending on the pattern string
            head = self.create_chain_of_objects()
            for i, letter in enumerate(target_string):
                result = head.handle(i, target_string)
                if result == -1 and i < len(target_string):
                    continue
                else:
                    return result
        return -1

    # Find the handler that matches the character in the pattern string and will handle it eventually
    def create_handler_from_character(self, pattern_index):
        character = self._pattern[pattern_index]
        if character == '.':
            handler = DotHandler(pattern_index, self._pattern)
        elif character == '*':
            handler = StarHandler(pattern_index, self._pattern)
        else:
            handler = RegularHandler(pattern_index, self._pattern)
        return handler

    # Create chain of objects depending on the pattern string
    def create_chain_of_objects(self, handler=None, pattern_index=0):
        # For the first handler, head, initialize the handler so that the next handlers can follow head
        if handler is None:
            handler = self.create_handler_from_character(pattern_index)
            handler = self.create_chain_of_objects(handler, pattern_index + 1)
        if pattern_index < len(self._pattern):
            new_handler = self.create_handler_from_character(pattern_index)
            if pattern_index + 1 < len(self._pattern):
                if handler._next_handler:
                    next_handler = handler._next_handler
                    # Follow the depth of the chain and attach the new handler to its end
                    new_handler = self.create_chain_of_objects(next_handler, pattern_index + 1)
                else:
                    new_handler = self.create_chain_of_objects(new_handler, pattern_index + 1)
                    handler.set_next(new_handler)
            else:
                handler.set_next(new_handler)
        return handler