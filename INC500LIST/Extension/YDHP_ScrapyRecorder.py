import datetime
from . import YDHP_ScrapySystem


class ScrapperRecorder:

    @property
    def time_consumed(self):
        return datetime.datetime.now() - self._time_consumed

    def time_consumed_string(self):
        return str(self.time_consumed)

    def __init__(self):
        self._time_consumed = datetime.datetime.now()

