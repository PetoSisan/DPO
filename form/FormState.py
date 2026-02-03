from enum import Enum

class FormState(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    DONE = 2
    ABORTED = 3
