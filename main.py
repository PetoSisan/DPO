from processes.xmlReader import read_XML
from processes.parser import parse
from processes.parser import get_project_id
from processes.loger import record
from processes.loger import find_missing_data

from datetime import datetime

from entities.Person import Person
from entities.Project import Project

from entities.Statement import Statement

from form.IFormManager import IFormManager
from GUI.GUIFormManager import GUIFormManager

from form.create_questions import create_questions


def main() -> int:
    error = ""

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M")

    applicants: list[Person] = []
    project_owners: list[Person] = []
    project: Project = None
    new_doc_name = ""
    data = None
    
    try:
        input_file = "šišan.xml" 
        data = read_XML(input_file)
        applicants, project_owners, project = parse(data)
        new_doc_name = f"{project.id} - DPO ({timestamp}).docx"
        
        form_manager: IFormManager = GUIFormManager(create_questions())

        if form_manager.wanted():
            form_manager.run()

        statement = Statement(applicants, project_owners, project, form_manager.form.qna, form_manager.form.state)
        statement.create()

    
    except FileNotFoundError as e:
        error = "Súbor sa nenašiel. Prosím skontrolujte, či zadaný súbor existuje v pracovnom adresári." \
                f" Vyhodená chyba: \n {str(e)} \n"
    
    except Exception as e:
        error = f"Počas behu programu sa objavila neočakávaná chyba :(. Vyhodená chyba: \n {str(e)} \n"
    

    record(error, now, new_doc_name, get_project_id(data, project),
           find_missing_data(applicants, project_owners))
    
    input("Press Enter to exit...")
    return 0 if error == "" else 1


if __name__ == "__main__":
    main()