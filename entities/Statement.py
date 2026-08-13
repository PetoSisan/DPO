from datetime import datetime
from shutil import copy

from entities.Person import Person
from entities.Project import Project
from form.Form import Form
from form.FormState import FormState
from processes.filler import fill_doc
from processes.parser import prepare_data

Question = str
Answer = str


class Statement:
    def __init__(
        self,
        applicants: list[Person],
        project_owners: list[Person],
        project: Project,
        form: Form,
        date_time: datetime = datetime.now(),
        template_name: str = "VZOR - Záväzné vyjadrenie DPO.docx",
    ):
        self.applicants = applicants
        self.project_owners = project_owners
        self.project = project
        self.form = form
        self.date_time = date_time

        self.template_name = template_name

    def create(self) -> None:
        new_doc_name = f"{self.project.id} - DPO.docx"

        if self.form.state == FormState.ABORTED:
            print("Upozornenie: Vypĺňanie formulára bolo prerušené.")
            print("Dáta vytiahnuté z formulára môžu byť nekompletné.")

        qna = {
            row_name: "".join(answers) for row_name, answers
            in self.form.qna.items()
        }
        header_data, data = prepare_data(
            self.applicants,
            self.project_owners,
            self.project,
            qna,
            self.date_time
        )

        copy(self.template_name, new_doc_name)
        fill_doc(new_doc_name, header_data, data, self.date_time)
