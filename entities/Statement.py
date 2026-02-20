from entities.Person import Person
from entities.Project import Project

from datetime import datetime


Question = str
Answer = str

from form.FormState import FormState

from processes.parser import prepare_data
from processes.filler import fill_doc

from shutil import copy


class Statement:
    def __init__(self, applicants: list[Person], project_owners: list[Person],
                 project: Project, qna: dict[Question, list[Answer]],
                 form_state: FormState, date_time: datetime = datetime.now(),
                 template_name: str = "VZOR - Záväzné vyjadrenie DPO.docx"):
        self.applicants = applicants
        self.project_owners = project_owners
        self.project = project
        self.qna = qna
        self.form_state = form_state
        self.date_time = date_time

        self.template_name = template_name


    def create(self) -> None:
        timestamp = self.date_time.strftime("%Y-%m-%d_%H-%M")
        new_doc_name = f"{self.project.id} - DPO ({timestamp}).docx"

        if self.form_state == FormState.ABORTED:
            print("Vypĺňanie formulára bolo prerušené.")

        qna = {row_name: str.join(answers) for row_name, answers in self.qna.items()}
        header_data, data = prepare_data(self.applicants, self.project_owners, self.project, qna, self.date_time)
        
        copy(self.template_name, new_doc_name)
        fill_doc(new_doc_name, header_data, data, self.date_time)

        return