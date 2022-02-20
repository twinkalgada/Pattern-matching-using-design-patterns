from Handler import Handler
from abc import ABC, abstractmethod
from typing import Optional

class AbstractHandler(Handler):
    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, position, target_string) -> Optional[int]:
        if self._next_handler:
            return self._next_handler.handle(position, target_string)

        return None