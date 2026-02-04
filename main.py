from processes.xmlReader import read_XML
from processes.parser import parse
from processes.parser import get_project_id

from datetime import datetime
from processes.filler import fill_doc
from processes.loger import log
from entities.Person import Person
from entities.Project import Project

from observer.Observer import Observer

from processes.parser import prepare_data

from form.Form import IForm
from form.form_wanted import form_wanted
from GUI.GUIForm import GUIForm


def main() -> int:
    error = ""

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M")

    applicants: list[Person] | None = None
    project_owners: list[Person] | None = None
    project: Project = None
    new_doc = ""
    data = None
    
    try:
        
        input_file = "šišan.xml" 
        data = read_XML(input_file)
        applicants, project_owners, project = parse(data)

        observer = Observer(applicants, project_owners, project, timestamp)

        wanted_form = form_wanted()

        if wanted_form:
            form: IForm = GUIForm({}) # TODO
            form.register_callback(observer.finish)
            form.run()

        
    
    except FileNotFoundError as e:
        error = "Súbor sa nenašiel. Prosím skontrolujte, či zadaný súbor existuje v pracovnom adresári." \
                f" Vyhodená chyba: \n {str(e)} \n"
    
    except Exception as e:
        error = f"Počas behu programu sa objavila neočakávaná chyba :(. Vyhodená chyba: \n {str(e)} \n"
    
    
    input("Press Enter to exit...")

    return 0 if error == "" else 1
        

if __name__ == "__main__":
    main()