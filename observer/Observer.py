Question = str
Answer = str

from ..form.Form import IForm
from ..form.FormState import FormState

from processes.filler import fill_doc
from processes.loger import record
from processes.loger import find_missing_data
from processes.parser import prepare_data

from entities.Person import Person
from entities.Project import Project

from datetime import datetime

from shutil import copy


class Observer:
    def __init__(self, applicants: list[Person], project_owners: list[Person],
                 project: Project, timestamp: str,
                 template_name: str = "VZOR - Záväzné vyjadrenie DPO.docx"):
        self.applicants = applicants
        self.project_owners = project_owners
        self.project = project
        self.timestamp = timestamp
        self.template_name = template_name


    def finish(self, qna: dict[Question, list[Answer]], state: FormState) -> int:
        """Callback"""
        new_doc_name = f"{self.project.id} - DPO ({self.timestamp}).docx"

        if state == FormState.ABORTED:
            print("Vypĺňanie formulára bolo prerušené.")

        qna = {row_name: str.join(answers) for row_name, answers in qna.items()}
        header_data, data = prepare_data(self.applicants, self.project_owners, self.project, qna)
        
        error = ""
        try:
            copy(self.template_name, new_doc_name)
            fill_doc(new_doc_name, header_data, data, self.timestamp)

        except FileNotFoundError as e:
            error = "Súbor sa nenašiel. Prosím skontrolujte, či zadaný súbor existuje v pracovnom adresári." \
                f" Vyhodená chyba: \n {str(e)} \n"
    
        except Exception as e:
            error = f"Počas behu programu sa objavila neočakávaná chyba :(. Vyhodená chyba: \n {str(e)} \n"

        record(error, self.timestamp, new_doc_name, self.project.id,
               find_missing_data(self.applicants, self.project_owners))
        return True if error == "" else False