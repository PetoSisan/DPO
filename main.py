from datetime import datetime

from entities.Person import Person
from entities.Project import Project
from entities.Statement import Statement
from form.create_form import create_form
from processes.loger import find_missing_data, record
from processes.parser import get_project_id, parse
from processes.xmlReader import read_XML
from UI.GUI.GUI import GUI


def DPO() -> int:
    error = ""

    now = datetime.now()

    applicants: list[Person] = []
    project_owners: list[Person] = []
    project: Project = None
    new_doc_name = ""
    data = None

    input_file = "šišan.xml"

    try:
        data = read_XML(input_file)
        applicants, project_owners, project = parse(data)
        new_doc_name = f"{project.id} - DPO.docx"

        form = create_form()
        gui = GUI()

        if gui.wanted():
            gui.run(form, project.id)

        statement = Statement(applicants, project_owners, project, form)
        statement.create()

    except FileNotFoundError as e:
        error = (
            "Súbor sa nenašiel. Prosím skontrolujte, či zadaný súbor existuje v pracovnom adresári."
            f" Vyhodená chyba: \n {e!s} \n"
        )

    except Exception as e:
        error = f"Počas behu programu sa objavila neočakávaná chyba :(. Vyhodená chyba: \n {e!s} \n"

    record(
        error,
        now,
        new_doc_name,
        get_project_id(data, project),
        find_missing_data(applicants, project_owners),
    )

    input("Press Enter to exit...")
    return 0 if error == "" else 1


def main() -> int:
    return DPO()


if __name__ == "__main__":
    main()
