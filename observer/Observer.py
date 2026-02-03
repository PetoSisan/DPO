Question = str
Answer = str

from ..form.Form import IForm
from ..form.FormState import FormState

from processes.filler import fill_doc

from datetime import datetime



class Observer:
    def __init__(self, new_doc: str, header_data: dict[str, str], data: dict[str, str]):
        self.new_doc = new_doc
        self.header_data = header_data
        self.data = data


    def finish(self, qna: dict[Question, list[Answer]], state: FormState) -> int:
        # """Callback"""
        # now = datetime.now()
        # timestamp = now.strftime("%Y-%m-%d_%H-%M")

        # fill_doc(self.new_doc, self.header_data, self.data, , timestamp)
        pass