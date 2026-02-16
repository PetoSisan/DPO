from processes.xmlReader import read_XML
from processes.parser import parse
from processes.parser import get_project_id
from processes.loger import record
from processes.loger import find_missing_data

from datetime import datetime

from entities.Person import Person
from entities.Project import Project

from observer.Observer import Observer

from form.Form import IForm
from form.form_wanted import form_wanted
from form.FormState import FormState
from GUI.GUIForm import GUIForm



def main() -> int:
    error = ""

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M")
    date = now.strftime("%d.%m.%Y")
    print(date)

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
        
        form: IForm = GUIForm({}) # TODO
        observer = Observer(applicants, project_owners, project, timestamp, date)
        wanted_form = form_wanted()

        if wanted_form:
            form.register_callback(observer.finish)
            retcode = form.run()
        else:
            observer.finish({}, FormState.NOT_STARTED)

    
    except FileNotFoundError as e:
        error = "Súbor sa nenašiel. Prosím skontrolujte, či zadaný súbor existuje v pracovnom adresári." \
                f" Vyhodená chyba: \n {str(e)} \n"
    
    except Exception as e:
        error = f"Počas behu programu sa objavila neočakávaná chyba :(. Vyhodená chyba: \n {str(e)} \n"
    
    if error != "":
        record(error, timestamp, new_doc_name, get_project_id(data, project),
               find_missing_data(applicants, project_owners))
    
    input("Press Enter to exit...")
    return 0


if __name__ == "__main__":
    main()